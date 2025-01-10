import json
import pandas as pd
import requests

from trip_check_api.consts import AUTHKEY

def get(path: str) -> dict:
    """Get dictionary of raw data from ODOT's TripCheck API."""
    if path[0] != '/':
        path = f"/{path}"
    request_url = f"http://api.odot.state.or.us/tripcheck/{path}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    response.raise_for_status()
    return json.loads(response.text)
