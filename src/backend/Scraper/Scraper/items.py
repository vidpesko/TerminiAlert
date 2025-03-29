# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime
from dataclasses import field, dataclass

import scrapy


@dataclass
class Slot:
    date: datetime | None = field(default=None)
    spots_left: int | None = field(default=None)
    exam_type: str | None = field(default=None)
    categories: list[str] = field(default_factory=list)
    duration: int | None = field(default=None)
    location_district: str | None = field(default=None)
    location: str | None = field(default=None)
