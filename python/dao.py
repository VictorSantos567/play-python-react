import requests

URL = "http://worldtimeapi.org/api/timezone/"

PAYLOAD = {}
HEADERS = {}


def get_all_area_as_json():
    response = requests.request("GET", URL, headers=HEADERS, data=PAYLOAD)
    res = response.json()
    return res

