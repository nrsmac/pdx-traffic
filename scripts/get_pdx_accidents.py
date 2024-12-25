import os
import requests
from dotenv import load_dotenv

from trip_check_api_client import Client
from trip_check_api_client.api.tle import tle_get_local_events_by_filter

load_dotenv()

AUTHKEY = os.getenv('TRIPCHECK_API_KEY')
PDX_BOUNDS = "-122.875228,45.414915,-122.631469,45.559331"

def get_accidents_with_requests():
    request_url = f"http://api.odot.state.or.us/tripcheck/Tle/Events?Bounds={PDX_BOUNDS}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    return response.text

def get_accidents():
    # request_url = f"Events?Bounds={PDX_BOUNDS}"
    client = Client(base_url="http://api.odot.state.or.us/tripcheck/") 
    client._headers.update({
        'Ocp-Apim-Subscription-Key': AUTHKEY
    })
    with client as client:
        accidents = tle_get_local_events_by_filter.sync_detailed(client=client, bounds=PDX_BOUNDS)
    # response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    print(accidents)
    return accidents

def write_accidents_to_json(raw_json):
    with open('pdx-acidents.json', "w+") as file:
        file.write(raw_json)

if __name__ == "__main__":
    # accidents_json = get_accidents_with_requests()
    accidents_json = get_accidents()
    # write_accidents_to_json(accidents_json)