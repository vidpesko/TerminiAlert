"""
Script, which manages all processes related to scraping. If periodically fetches all reminders from db, enumerates them and scrapes websites.

Process - every x minutes/hours:
    1. Fetch all reminders from db
    2. Enumerates reminders and runs spider for each
    3. Sends emails if needed

"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

try:
    import shared
except ModuleNotFoundError:
    sys.path.append(str(Path.cwd().parent.parent))
finally:
    from shared.db.models import Reminder, AvpSlot
    from shared.config import settings

from manager_utils import REMINDER_HANDLING_TABLE, send_mail
from shared.config import settings


MANAGER_WAIT_TIME_MINUTES = 0.1  # How often to run manager iteration (in minutes)


# Global sqlalchemy engine instance
engine = create_engine(settings.create_engine_url())


def run_spider(spider_name: str, urls: list[str]):
    result = subprocess.run(
        ["./run_spider.sh", spider_name, *urls],
        capture_output=True,
        text=True,
    )

    # print(result.stderr)

    # TODO Add error / success checking


def run_manager_iteration():
    # Main process - starts manager process
    # 1. Fetch reminders
    with Session(engine) as session:
        reminders = session.query(Reminder).all()

        for reminder in reminders:
            # 2. Run spider
            # Get spider name and url gen function
            print("Current reminder:", reminder.email, reminder.current_date)
            service = REMINDER_HANDLING_TABLE.get(reminder.service_name)

            if not service:
                raise Exception(
                    f"For service type '{reminder.service_name}', there is no entry in REMINDER_HANDLING_TABLE"
                )

            spider_name, url_gen_func = service

            if not reminder.service_url:
                url = url_gen_func(reminder.filters)
                reminder.service_url = url
            else:
                url = reminder.service_url

            response = run_spider(spider_name, [url, ])  # TODO Check if response returns error

            # 3. Send emails (if needed)
            slots = session.query(AvpSlot).where(AvpSlot.service_url == url).order_by(AvpSlot.date).all()
            nearest_slot = slots[0]

            if (nearest_slot.date < reminder.current_date):
                if (reminder.suggested_date and (nearest_slot.date < reminder.suggested_date)) or not reminder.suggested_date:
                    # Add date to found dates. If user accepts the date, it will be set to suggested_date
                    if not reminder.found_dates:
                        reminder.found_dates = []
                    # check if date already in found_dates
                    for found_date in reminder.found_dates:
                        if found_date["date"] == nearest_slot.date.strftime("%Y-%m-%d %H:%M:%S"):
                            break
                    else:
                        reminder.found_dates.append(
                            {
                                "date": nearest_slot.date.strftime("%Y-%m-%d %H:%M:%S"),
                                "id": nearest_slot.slot_id,
                                "index": len(reminder.found_dates),
                                "status": "needs_action", # needs_action, accepted, declined
                            }
                        )
                        flag_modified(reminder, "found_dates")

                        context = {
                            "current_exam_date": reminder.current_date.strftime("%d.%m.%Y ob %H:%M"),
                            "earlier_slot_date": nearest_slot.date.strftime("%d.%m.%Y ob %H:%M"),
                            "test_center_name_or_location": "Ljubljana Center",
                            "test_type": "Vožnja",
                            "accept_slot_link": settings.frontend_base_url
                            + f"/domov?id={reminder.reminder_id}&action=potrdi&slot_id={nearest_slot.slot_id}",
                            "decline_slot_link": settings.frontend_base_url
                            + f"/domov?id={reminder.reminder_id}&action=zavrni&slot_id={nearest_slot.slot_id}",
                            "unsubscribe_link": settings.frontend_base_url
                            + f"/domov?id={reminder.reminder_id}&action=izbris",
                        }
                        send_mail(reminder.email, context)

            # 4. Delete slots
            session.query(AvpSlot).filter(AvpSlot.service_url == url).delete()

            session.commit()


def start_manager():
    # Start periodically running manager
    print(f"Started manager at {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    while True:
        run_manager_iteration()
        sleep(MANAGER_WAIT_TIME_MINUTES * 60)  # Convert minutes to seconds


if __name__ == "__main__":
    start_manager()
