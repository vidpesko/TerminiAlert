"""
This file contains url generating functions for every supported service. When manager has to handle a reminder, it will use table at the bottom to retireve spider name and function for generating urls
"""


def avp_url_generator(filters: dict) -> str:
    return "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&cat=-&type=VSE&type=2&type=1&izpitniCenter=20&lokacija=194&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1"


REMINDER_HANDLING_TABLE = {
    "avp": ("avp", avp_url_generator)
    # service_name (as in db): (spider name, url generating function)
}
