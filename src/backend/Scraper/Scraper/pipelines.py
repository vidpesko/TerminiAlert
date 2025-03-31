import sys
from pathlib import Path
from collections import defaultdict

from itemadapter import ItemAdapter

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session

from .items import Slot, SlotsResult

try:
    import shared
except ModuleNotFoundError:
    sys.path.append(str(Path.cwd().parent.parent))
finally:
    from shared.db.models import AvpSlot, Reminder
    from shared.config import settings


engine = create_engine(settings.create_engine_url())


class SlotPipeline:
    def process_item(self, item: SlotsResult, spider):
        adapter = ItemAdapter(item)

        # Save to db
        with Session(engine) as session:
            # Group same slots -> increase spots_left by number of same slots and delete all but one
            slots = adapter.get("slots")
            grouped = defaultdict(list)

            url = spider.start_urls[0]
            reminder = session.query(Reminder).where(Reminder.service_url == url).first()

            for slot in slots:
                slot_adapter = ItemAdapter(slot)
                key = str(list(slot_adapter.values()))
                grouped[key].append(slot)


            db_slots = []

            for key, value in grouped.items():
                if len(value) > 1:
                    slot = value[0]
                    slot.spots_left += len(value) - 1
                    grouped[key] = [slot, ]

                value = grouped[key]
                slot_item = value[0]
                slot_adapter = ItemAdapter(slot_item)

                slot_db = AvpSlot(service_name="avp", service_url=url, **dict(slot_adapter.items()))
                db_slots.append(slot_db)

            # Delete all slots with same filters
            slots_deleted = session.query(AvpSlot).where(AvpSlot.service_url == url).delete()

            # Add new slots
            for slot in db_slots:
                session.add(slot)

            session.commit()

        return item
