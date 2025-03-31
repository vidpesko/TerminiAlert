import json
from pathlib import Path

import scrapy

from ..items import Slot, SlotLoader, SlotsResult


class AvpSpider(scrapy.Spider):
    name = "avp"

    start_urls = [
        "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?type=2&cat=4&cat=1&izpitniCenter=18&lokacija=-1&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1",
    ]

    custom_settings = {
        "ITEM_PIPELINES": {
            "Scraper.pipelines.SlotPipeline": 290,
        }
    }

    def __init__(self, start_urls: list=None, urls: str=None, name=None, **kwargs):
        super().__init__(name, **kwargs)
        # Check if start_urls have been provided as argument to init

        if start_urls:
            self.start_urls = start_urls

        if urls:
            self.start_urls = json.loads(urls) if urls else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        slots = []

        for event in response.css(".dogodek"):
            slot = SlotLoader(item=Slot(), response=response, selector=event)
            # Date
            start_time = event.xpath(".//div[contains(text(), 'Začetek ob')]//span/text()").get()  # Start time
            date = event.css(".calendarBox::attr('aria-label')").get()
            slot.add_value("date", f"{date} {start_time}")
            # Spots
            slot.add_css("spots_left", ".contentOpomnik > .lessImportant::text")
            # Exam type
            slot.add_css("exam_type", ".contentOpomnik > div:nth-of-type(2)::text")
            # Categories
            slot.add_xpath("categories", ".//div[contains(text(), 'Kategorije:')]//span/text()")
            # Duration
            slot.add_xpath(
                "duration",
                ".//div[contains(text(), 'Začetek ob')]/text()[last()]",
            )
            # Location
            slot.add_css("location_district", ".upperOpomnikDiv > span::text")
            slot.add_css("location", ".upperOpomnikDiv > span:nth-of-type(2)::text")

            slot_item = slot.load_item()
            slots.append(slot_item)

        yield SlotsResult(0, slots)
