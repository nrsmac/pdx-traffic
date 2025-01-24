from dagster import asset
import pandas as pd
import trip_check_api.metadata as md


@asset
def incident_event_types() -> pd.DataFrame:
    return md.get_incident_event_types()


@asset
def incident_event_subtypes() -> pd.DataFrame:
    return md.get_incident_event_subtypes()


@asset
def road_condition_descriptions() -> pd.DataFrame:
    return md.get_road_condition_descriptions()


@asset
def weather_condition_descriptions() -> pd.DataFrame:
    return md.get_weather_condition_descriptions()


@asset
def routes() -> pd.DataFrame:
    return md.get_routes()


@asset
def travel_impact_descriptions() -> pd.DataFrame:
    return md.get_travel_impact_descriptions()


@asset
def travel_incident_types() -> pd.DataFrame:
    return md.get_travel_incident_types()
