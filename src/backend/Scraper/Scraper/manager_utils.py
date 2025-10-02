"""
This file contains url generating functions for every supported service. When manager has to handle a reminder, it will use table at the bottom to retireve spider name and function for generating urls
"""

import datetime
from urllib.parse import urlencode

from mailjet_rest import Client
from premailer import transform
from jinja2 import Environment, FileSystemLoader

from shared.config import settings


EMAIL_ADDRESS = "spletneresitve1@gmail.com"
EMAIL_APP_PASSWORD = "ensq kzpe rvig fvtc"  # App password for the gmail account


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


def send_mail(to: str, context: dict, subject = "Najden je bil nov termin"):
    # Render html template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("email.html")

    rendered_html = template.render(context)

    mailjet = Client(auth=(settings.mailjet_api_key, settings.mailjet_api_secret), version="v3.1")
    data = {
        "Messages": [
            {
                "From": {"Email": settings.from_email, "Name": settings.from_name},
                "To": [{"Email": to, "Name": context.get("user_name", "Uporabnik")}],
                "Subject": "Termini Alert - Najden je bil nov termin",
                "HTMLPart": rendered_html,
            }
        ]
    }
    result = mailjet.send.create(data=data)

    return result.status_code, result.json()


REMINDER_HANDLING_TABLE = {
    "avp": ("avp", avp_url_generator)
    # service_name (as in db): (spider name, url generating function)
}


# if __name__ == "__main__":
