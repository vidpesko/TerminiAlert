from pathlib import Path

import scrapy

from ..items import Slot


class AvpSpider(scrapy.Spider):
    name = "avp"

    start_urls = [
        "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&cat=-&type=1&izpitniCenter=19&lokacija=157&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1",
    ]

    def parse(self, response):
        for event in response.css(".dogodek"):
            slot = Slot()
            # Date
            date = event.css(".calendarBox::attr('aria-label')").get()
            print()

            # yield None
