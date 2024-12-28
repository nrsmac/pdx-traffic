import json
import os
import clickhouse_connect
import pandas as pd
import polars as pl
from dagster import AssetExecutionContext, asset
from dotenv import load_dotenv
import requests
from dags.postgres import upsert_to_postgres

load_dotenv()

# client = clickhouse_connect.get_client(host='localhost', port=8123, username='', password='')

AUTHKEY = os.getenv('TRIPCHECK_API_KEY')
PDX_BOUNDS = "-122.875228,45.414915,-122.631469,45.559331"


def get_accidents_with_requests():
    request_url = f"http://api.odot.state.or.us/tripcheck/Tle/Events?Bounds={PDX_BOUNDS}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    return response.text

def accidents():
    pass

def road_conditions():
    pass

@asset(compute_kind='source')
def traffic_detector_inventory(context: AssetExecutionContext):
    request_url = f"http://api.odot.state.or.us/tripcheck/TrafficDetector/inventory"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']
    tdl = data['traffic-detector-list']
    df = pd.DataFrame(tdl)

    df = pd.concat(
        (df['location'].apply(pd.series),
        df['detector-station'].apply(pd.series)),
        axis=1
    )

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)
    df['last-update-time'] = last_updated

    context.log.debug(df.columns)
    upsert_to_postgres(table_name=''.join(context.asset_key.path), df=df, primary_keys=['"location-id"','"station-id"'])
    return df

@asset(compute_kind='source')
def traffic_detector_road_data(context: AssetExecutionContext):
    request_url = f"http://api.odot.state.or.us/tripcheck/TrafficDetector/Roadway"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    detector_data_items = data['detector-data-items']

    df = pd.DataFrame(detector_data_items)['detector-list'].apply(pd.Series)['detector-data-detail'].apply(pd.Series)
    df['last-update-time'] = last_updated

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)

    upsert_to_postgres(table_name=''.join(context.asset_key.path), df=df, primary_keys=['"detector-id"','"lane"','"detection-time-stamp"'])
    return df

@asset(compute_kind='source')
def traffic_detector_road_data(context: AssetExecutionContext):
    request_url = f"http://api.odot.state.or.us/tripcheck/TrafficDetector/Roadway"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    data = json.loads(response.text)
    last_updated = data['organization-information']['last-update-time']

    detector_data_items = data['detector-data-items']

    df = pd.DataFrame(detector_data_items)['detector-list'].apply(pd.Series)['detector-data-detail'].apply(pd.Series)
    df['last-update-time'] = last_updated

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)

    upsert_to_postgres(table_name=''.join(context.asset_key.path), df=df, primary_keys=['"detector-id"','"lane"','"detection-time-stamp"'])
    return df

@asset(compute_kind='source')
def rwis_status(context: AssetExecutionContext):
    """Road Conditions"""
    request_url = f"http://api.odot.state.or.us/tripcheck/v2/Rwis/Status?Bounds={PDX_BOUNDS}"
    response = requests.get(request_url, headers={'Ocp-Apim-Subscription-Key':AUTHKEY})
    context.log.debug(response)
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

    object_columns = df.select_dtypes(include=['object']).columns
    df[object_columns] = df[object_columns].astype(str)

    upsert_to_postgres(table_name=''.join(context.asset_key.path), df=df, primary_keys=['"station-id"','"last-update-time"'])
    return df

def main():
    df = traffic_detector_inventory()
    print(df.head())
if __name__ == "__main__":
    main()
    # insert_df_to_clickhouse(df, 'traffic_detector_inventory')
