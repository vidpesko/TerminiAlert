from pathlib import Path

import scrapy

from ..items import Slot, SlotLoader


class AvpSpider(scrapy.Spider):
    name = "avp"

    start_urls = [
        "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&cat=-&type=1&izpitniCenter=19&lokacija=157&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1",
    ]

    def parse(self, response):
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
            yield slot_item
