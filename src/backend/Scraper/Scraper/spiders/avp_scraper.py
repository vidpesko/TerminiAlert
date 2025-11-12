import json

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

        raw_slots = zip(response.css(".js_dogodekBox"), response.css(".js_dicDetails"))

        current_date = None
        for event, event_details in raw_slots:
            slot = SlotLoader(item=Slot(), response=response, selector=event)
            # Date
            start_time = event.css('td[data-th="Ura"]::text').get().strip()  # Start time
            date = event.css(".calendarBox::attr('aria-label')").get()
            if date:
                current_date = date
            else:
                date = current_date
            slot.add_value("date", f"{date} {start_time}")
            # Spots
            slot.add_css("spots_left", 'td[data-th="Prosta mesta"]::text')
            # Exam type
            slot.add_value(
                "exam_type",
                event_details.xpath('normalize-space(//tr[@class="js_dicDetails dicDetails"]/td/text()[last()])').get()
            )
            # Categories
            slot.add_xpath("categories", 'normalize-space(//td[@data-th="Kategorije"])')
            # Duration
            slot.add_value("duration", 0) # ! AVP removed duration info
            # Location
            slot.add_css("location_district", ".dicDisclaimer::text")
            slot.add_value("location", event_details.css(".dicTitle2::text").get())

            slot_item = slot.load_item()
            slots.append(slot_item)

        yield SlotsResult(0, slots)
