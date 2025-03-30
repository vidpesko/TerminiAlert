import sys
import typing
import time
import importlib
import pkgutil
from types import ModuleType

import scrapy
from scrapy.utils.spider import iter_spider_classes

import pipelines
from middlewares import ScraperDownloaderMiddleware
from spiders.avp_scraper import AvpSpider


def generate_exception_response(description: str, exception: Exception):
    return {
        "exception": True,
        "exception_type": "scraper_exception",
        "description": description,
        "str": str(exception),
        "repr": repr(exception),
    }


def load_pipelines(pipelines_dict: list[dict]) -> list[ModuleType]:
    ordered_pipelines = list(pipelines_dict.items())
    ordered_pipelines.sort(key=lambda x: x[1])

    # Import pipelines
    imported_pipelines = []
    for pipeline in ordered_pipelines:
        # Split the module and class name
        module_name, class_name = pipeline[0].rsplit(".", 1)
        cls = getattr(pipelines, class_name)
        cls_instance = cls()
        imported_pipelines.append(cls_instance)

    return imported_pipelines


def get_spider_from_name(
    spider_name, spiders_module="spiders"
) -> typing.Type[scrapy.Spider]:
    module = importlib.import_module(spiders_module)

    for _, module_name, is_pkg in pkgutil.iter_modules(module.__path__):
        if not is_pkg:
            spider_module = importlib.import_module(f"{spiders_module}.{module_name}")
            for cls in iter_spider_classes(spider_module):
                if cls.name == spider_name:
                    return cls

    raise ValueError(f"No spider with name '{spider_name}' exists")


def run_spider(
    Spider: typing.Type[scrapy.Spider] | str, parameters: dict | None = None
) -> list[scrapy.Item]:
    if isinstance(Spider, str):
        Spider = get_spider_from_name(Spider)

    pipelines = Spider.custom_settings.get("ITEM_PIPELINES")
    if pipelines:
        imported_pipelines = load_pipelines(pipelines)

    if not parameters:
        parameters = {}

    # If spider name is provided
    if isinstance(Spider, str):
        _spider = get_spider_from_name(Spider)
        spider = _spider(**parameters)
    else:
        spider = Spider(**parameters)

    output = []

    for request in spider.start_requests():
        middleware = ScraperDownloaderMiddleware()

        try:
            response = middleware.process_request(request, spider)
            print(response)
        except TimeoutError as exc:
            exception = generate_exception_response("Timeout reached", exc)
            output.append(exception)
            continue
        except Exception as exc:
            exception = generate_exception_response("Exception has occured", exc)
            output.append(exception)
            continue

        # Process items using pipelines
        if pipelines:
            for item in spider.parse(response):
                for pipeline in imported_pipelines:
                    item = pipeline.process_item(item, spider)
                output.append(item)

    return output


if __name__ == "__main__":
    start = time.perf_counter()
    items = run_spider(AvpSpider)
    print(items)
    print("Execution took:", time.perf_counter() - start, "seconds")
