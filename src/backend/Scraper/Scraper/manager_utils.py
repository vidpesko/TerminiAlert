"""
This file contains url generating functions for every supported service. When manager has to handle a reminder, it will use table at the bottom to retireve spider name and function for generating urls
"""

from urllib.parse import urlencode


def avp_url_generator(filters: dict) -> str:
    filters_keys_translation_table = {
        "exam_type": "type",
        "categories": "cat",
        "location_district": "izpitniCenter",
        "location": "lokacija",
    }

    default_url_params = {
        "type": "-",
        "cat": "-",
        "izpitniCenter": -1,
        "lokacija": -1,
        "offset": 0,
        "sentinel_type": "ok",
        "sentinel_status": "ok",
        "is_ajax": 1
    }

    _filters = default_url_params

    for key, val in filters.items():
        new_key = filters_keys_translation_table.get(key, key)
        _filters[new_key] = val

    url = "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?"
    url_params = urlencode(_filters, doseq=True)

    return url + url_params


REMINDER_HANDLING_TABLE = {
    "avp": ("avp", avp_url_generator)
    # service_name (as in db): (spider name, url generating function)
}
