# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
from datetime import datetime
from dataclasses import field, dataclass


from itemloaders.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.loader import ItemLoader


VALUES_TRANSLATION_TABLE = {
    "Preverjanje znanja vožnje": "driving",
    "Preverjanje znanja teorije": "theory",
}


@dataclass
class Slot:
    date: datetime | None = field(default=None)
    spots_left: int | None = field(default=None)
    exam_type: str | None = field(default=None)
    categories: list[str] = field(default_factory=list)
    duration: int | None = field(default=None)
    location_district: str | None = field(default=None)
    location: str | None = field(default=None)


class SlotLoader(ItemLoader):
    default_output_processor = TakeFirst()

    date_in = MapCompose(lambda x: datetime.strptime(x, "%d. %m. %Y %H:%M"))

    spots_left_in = MapCompose(
        lambda x: int(re.search(r"Še\s*(\d+)\s*", x).group(1))
    )

    exam_type_in = MapCompose(lambda x: VALUES_TRANSLATION_TABLE.get(x, x))

    categories_in = MapCompose(lambda x: x.replace(",", ""))
    categories_out = Identity()

    duration_in = MapCompose(lambda x: int(re.search(r"\(\s*trajanje\s*(\d+)\s*minut\s*\)", x).group(1)))

    location_in = MapCompose(lambda x: x.removeprefix(", "))


@dataclass
class SlotsResult:
    num_of_all_results: int
    slots: list[Slot]
