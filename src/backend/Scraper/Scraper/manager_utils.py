"""
This file contains url generating functions for every supported service. When manager has to handle a reminder, it will use table at the bottom to retireve spider name and function for generating urls
"""

import datetime
from urllib.parse import urlencode

import yagmail
import requests
from premailer import transform
from jinja2 import Environment, FileSystemLoader


EMAIL_ADDRESS = "spletneresitve1@gmail.com"
EMAIL_APP_PASSWORD = "ensq kzpe rvig fvtc"  # App password for the gmail account

EMAIL_HTML = """
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Najden je bil termin</title>
    <style>
        /* Basic reset */
        body,
        table,
        td,
        a {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        table {
            border-collapse: collapse !important;
        }

        img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            display: block;
        }

        body {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #f4f6f8;
            color: #0b1140;
        }

        /* Container */
        .email-wrapper {
            width: 100%;
            max-width: 600px;
            margin: 24px auto;
            background: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 24px rgba(13, 24, 57, 0.08);
        }

        /* Header image */
        .hero {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Content */
        .content {
            padding: 20px 24px;
        }

        h1 {
            margin: 0 0 8px 0;
            font-size: 20px;
            line-height: 1.2;
            color: #07123a;
        }

        p {
            margin: 0 0 14px 0;
            font-size: 15px;
            color: #24304e;
            line-height: 1.45;
        }

        /* CTA */
        .btn {
            display: inline-block;
            padding: 12px 18px;
            background: #ff7a59;
            color: #fff !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            box-shadow: 0 6px 18px rgba(255, 122, 89, 0.18);
        }

        .muted {
            color: #68708a;
            font-size: 13px;
        }

        /* Small details */
        .meta {
            background: #f7fafc;
            padding: 12px 16px;
            border-radius: 8px;
            margin: 14px 0;
            color: #253150;
            font-size: 14px;
        }

        .small {
            font-size: 13px;
            color: #667085;
        }

        /* Footer */
        .footer {
            padding: 18px 24px;
            font-size: 12px;
            color: #9aa0b4;
            text-align: center;
        }

        /* Mobile */
        @media only screen and (max-width:420px) {
            .content {
                padding: 16px;
            }

            h1 {
                font-size: 18px;
            }

            .btn {
                width: 100%;
                text-align: center;
            }
        }
    </style>
</head>

<body>
    <center style="width:100%; background:#f4f6f8; padding:24px 12px;">
        <table role="presentation" width="100%" style="max-width:600px;">
            <tr>
                <td>
                    <div class="email-wrapper" role="article" aria-label="Earlier slot found notification from {{APP_NAME}}">
                        <div class="content">
                            <h1>Good news, {{user_name}} — an earlier slot is available!</h1>

                            <p>
                                We found a new driving exam slot earlier than your current booking on <strong>{{current_exam_date}}</strong>. An earlier slot on <strong>{{earlier_slot_date}}</strong> is available.
                            </p>

                            <div class="meta" role="region" aria-label="Slot details">
                                <div style="font-weight:600;">Available slot</div>
                                <div style="margin-top:6px;">📅 <strong>{{earlier_slot_date}}</strong></div>
                                <div style="margin-top:6px;">📍 {{test_center_name_or_location}}</div>
                            </div>

                            <p style="margin-bottom:18px;">
                                If you want that earlier slot, tap the button below to claim it now — slots fill fast.
                            </p>

                            <p style="text-align:left;">
                                <a href="{{slot_link}}" class="btn" target="_blank" rel="noopener noreferrer">
                                    View & claim slot
                                </a>
                            </p>

                            <p class="small" style="margin-top:14px;">
                                Tip: If the link doesn't work, copy & paste this URL into your browser:
                                <br>
                                <a href="{{slot_link}}" style="color:#1b4dbc; word-break:break-all;">
                                    {{slot_link}}
                                </a>
                            </p>

                            <hr style="border:none; border-top:1px solid #eef2f7; margin:18px 0;">

                            <p class="muted">
                                You asked <strong>{{APP_NAME}}</strong> to notify you when earlier exam
                                slots become available. If you no longer want these alerts, you can
                                <a href="{{manage_prefs_link}}" style="color:#1b4dbc;">
                                    manage your preferences
                                </a> or
                                unsubscribe below.
                            </p>
                        </div>

                        <div class="footer">
                            <div style="margin-bottom:8px;">
                                Sent by
                                <a href="termini.pesko.si">termin.si</a>
                            </div>
                            <div class="small">
                                <a href="{{support_link}}" style="color:#1b4dbc;">
                                    Support
                                </a>
                                ·
                                <a href="{{unsubscribe_link}}" style="color:#1b4dbc;">
                                    Unsubscribe
                                </a>
                            </div>
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </center>
</body>

</html>
"""


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


def send_mail(to: str, new_date: datetime.datetime, subject = "Najden je bil nov termin"):
    # Render html template
    # env = Environment(loader=FileSystemLoader('.'))
    # template = env.get_template("email.html")

    context = {"user_name": "John Doe", "earlier_slot_date": new_date.strftime("%d.%m.%Y %H:%M")}
    context = {
        "APP_NAME": "DriveAlert",
        "user_name": "John Doe",
        "current_exam_date": "2025-10-15",
        "earlier_slot_date": "2025-10-10",
        "test_center_name_or_location": "Ljubljana Center",
        "slot_link": "https://example.com/slot",
        "manage_prefs_link": "https://example.com/manage",
        "company_address": "123 Street, Ljubljana",
        "support_link": "https://example.com/support",
        "unsubscribe_link": "https://example.com/unsubscribe",
    }
    # rendered_html = template.render(context)

    # yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
    # contents = yagmail.raw(transform(EMAIL_HTML))
    # yag.send(to, subject, contents)


REMINDER_HANDLING_TABLE = {
    "avp": ("avp", avp_url_generator)
    # service_name (as in db): (spider name, url generating function)
}
