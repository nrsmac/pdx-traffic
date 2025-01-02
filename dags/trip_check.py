import json
import os

from dotenv import load_dotenv
import pandas as pd
import requests

load_dotenv()
AUTHKEY = os.getenv('TRIPCHECK_API_KEY')
PDX_BOUNDS = "-122.875228,45.414915,-122.631469,45.559331"

def get_cls_inventory_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/Cls/Inventory"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    cls_inventory = data['cls-inventory-items']

    df = pd.DataFrame(cls_inventory).apply(pd.Series)
    df['last-update-time'] = last_updated

    df = _cast_object_columns_to_string(df)
    return df


def get_rwis_inventory_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/v2/Rwis/Inventory?Bounds={PDX_BOUNDS}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    ess_site_list = data['ess-site-list']

    df = pd.DataFrame(ess_site_list).apply(pd.Series)
    df['last-update-time'] = last_updated

    df = _cast_object_columns_to_string(df)

    return df

def get_traffic_detector_inventory_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/TrafficDetector/inventory"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']
    tdl = data['traffic-detector-list']
    df = pd.DataFrame(tdl)

    df = pd.concat(
        (df['location'].apply(pd.Series),
        df['detector-station'].apply(pd.Series)),
        axis=1
    )
    df['last-update-time'] = last_updated
    df = _cast_object_columns_to_string(df)
    return df

def get_traffic_detector_road_data_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/TrafficDetector/Roadway"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    detector_data_items = data['detector-data-items']

    df = pd.DataFrame(detector_data_items)['detector-list'].apply(pd.Series)['detector-data-detail'].apply(pd.Series)
    df['last-update-time'] = last_updated

    df = _cast_object_columns_to_string(df)
    return df

def get_cls_speed_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/Cls/Speed"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    cls_inventory = data['CLS-inventory']

    df = pd.DataFrame(cls_inventory).apply(pd.Series)
    df['last-update-time'] = last_updated

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)
    return df

def get_rwis_status_df():
    request_url = f"http://api.odot.state.or.us/tripcheck/v2/Rwis/Status?Bounds={PDX_BOUNDS}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    weather_stations = data['WeatherStations']

    df = pd.DataFrame(weather_stations)
    df = pd.concat(
        (
            df['station-id'],
            df['RoadWeather'].apply(pd.Series),
            df['SurfaceCondition'].apply(pd.Series)
        )
       ,
       axis=1
    )
    df['last-update-time'] = last_updated

    df = _cast_object_columns_to_string(df)
    return df

def _cast_object_columns_to_string(df) -> pd.DataFrame:
    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)
    return df

