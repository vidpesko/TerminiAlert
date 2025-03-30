import sys
from pathlib import Path

from itemadapter import ItemAdapter

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .items import Slot

try:
    import shared
except ModuleNotFoundError:
    sys.path.append(str(Path.cwd().parent.parent))
finally:
    from shared.db.models import AvpSlot
    from shared.config import settings


engine = create_engine(settings.create_engine_url())


class SlotPipeline:
    def process_item(self, item: Slot, spider):
        adapter = ItemAdapter(item)

        # Save to db
        with Session(engine) as session:
            slot = AvpSlot(service_name="avp", **dict(adapter.items()))
            

        return item
