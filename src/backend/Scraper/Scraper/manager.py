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

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

try:
    import shared
except ModuleNotFoundError:
    sys.path.append(str(Path.cwd().parent.parent))
finally:
    from shared.db.models import Reminder, AvpSlot
    from shared.config import settings

from manager_utils import REMINDER_HANDLING_TABLE


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


def start_manager():
    # Main process - starts manager process
    # 1. Fetch reminders
    with Session(engine) as session:
        reminders = session.query(Reminder).all()

        # r = Reminder(email="vid@pesko.si", service_name="avp", current_date=datetime(2025, 4, 20, 12, 30), filters={
        #     "type": 2,
        #     "cat": [4, 1],
        #     "izpitniCenter": 18
        # })
        # session.add(r)
        # session.commit()

        for reminder in reminders:
            # 2. Run spider
            # Get spider name and url gen function
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

            if (nearest_slot.date < reminder.current_date) and (nearest_slot.date < reminder.suggested_date):
                reminder.suggested_date = nearest_slot.date

            # if reminder.suggested_date
            # session.query()

        session.commit()


if __name__ == "__main__":
    # run_spider(
    #     "avp",
    #     [
    #         "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&cat=-&type=VSE&type=2&type=1&izpitniCenter=20&lokacija=194&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1"
    #     ],
    # )

    start_manager()
