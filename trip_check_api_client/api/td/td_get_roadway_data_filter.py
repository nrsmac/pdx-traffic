from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.td_roadway_data import TDRoadwayData
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    jurisdiction_id: Union[Unset, str] = UNSET,
    location_id: Union[Unset, str] = UNSET,
    highway_name: Union[Unset, str] = UNSET,
    milepoint: Union[Unset, str] = UNSET,
    station_id: Union[Unset, str] = UNSET,
    station_class: Union[Unset, str] = UNSET,
    ramp_id: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["JurisdictionId"] = jurisdiction_id

    params["LocationId"] = location_id

    params["HighwayName"] = highway_name

    params["Milepoint"] = milepoint

    params["StationId"] = station_id

    params["StationClass"] = station_class

    params["RampId"] = ramp_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/TrafficDetector/Roadway",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, TDRoadwayData]]:
    if response.status_code == 200:
        response_200 = TDRoadwayData.from_dict(response.json())



        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, TDRoadwayData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    jurisdiction_id: Union[Unset, str] = UNSET,
    location_id: Union[Unset, str] = UNSET,
    highway_name: Union[Unset, str] = UNSET,
    milepoint: Union[Unset, str] = UNSET,
    station_id: Union[Unset, str] = UNSET,
    station_class: Union[Unset, str] = UNSET,
    ramp_id: Union[Unset, str] = UNSET,

) -> Response[Union[Any, TDRoadwayData]]:
    """ Traffic Detector Roadway Data

     Roadway traffic detectors collecting volume, occupancy and speed data from select roadways located
    in Oregon

    Args:
        jurisdiction_id (Union[Unset, str]):
        location_id (Union[Unset, str]):
        highway_name (Union[Unset, str]):
        milepoint (Union[Unset, str]):
        station_id (Union[Unset, str]):
        station_class (Union[Unset, str]):
        ramp_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TDRoadwayData]]
     """


    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
location_id=location_id,
highway_name=highway_name,
milepoint=milepoint,
station_id=station_id,
station_class=station_class,
ramp_id=ramp_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    jurisdiction_id: Union[Unset, str] = UNSET,
    location_id: Union[Unset, str] = UNSET,
    highway_name: Union[Unset, str] = UNSET,
    milepoint: Union[Unset, str] = UNSET,
    station_id: Union[Unset, str] = UNSET,
    station_class: Union[Unset, str] = UNSET,
    ramp_id: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, TDRoadwayData]]:
    """ Traffic Detector Roadway Data

     Roadway traffic detectors collecting volume, occupancy and speed data from select roadways located
    in Oregon

    Args:
        jurisdiction_id (Union[Unset, str]):
        location_id (Union[Unset, str]):
        highway_name (Union[Unset, str]):
        milepoint (Union[Unset, str]):
        station_id (Union[Unset, str]):
        station_class (Union[Unset, str]):
        ramp_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TDRoadwayData]
     """


    return sync_detailed(
        client=client,
jurisdiction_id=jurisdiction_id,
location_id=location_id,
highway_name=highway_name,
milepoint=milepoint,
station_id=station_id,
station_class=station_class,
ramp_id=ramp_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    jurisdiction_id: Union[Unset, str] = UNSET,
    location_id: Union[Unset, str] = UNSET,
    highway_name: Union[Unset, str] = UNSET,
    milepoint: Union[Unset, str] = UNSET,
    station_id: Union[Unset, str] = UNSET,
    station_class: Union[Unset, str] = UNSET,
    ramp_id: Union[Unset, str] = UNSET,

) -> Response[Union[Any, TDRoadwayData]]:
    """ Traffic Detector Roadway Data

     Roadway traffic detectors collecting volume, occupancy and speed data from select roadways located
    in Oregon

    Args:
        jurisdiction_id (Union[Unset, str]):
        location_id (Union[Unset, str]):
        highway_name (Union[Unset, str]):
        milepoint (Union[Unset, str]):
        station_id (Union[Unset, str]):
        station_class (Union[Unset, str]):
        ramp_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TDRoadwayData]]
     """


    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
location_id=location_id,
highway_name=highway_name,
milepoint=milepoint,
station_id=station_id,
station_class=station_class,
ramp_id=ramp_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    jurisdiction_id: Union[Unset, str] = UNSET,
    location_id: Union[Unset, str] = UNSET,
    highway_name: Union[Unset, str] = UNSET,
    milepoint: Union[Unset, str] = UNSET,
    station_id: Union[Unset, str] = UNSET,
    station_class: Union[Unset, str] = UNSET,
    ramp_id: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, TDRoadwayData]]:
    """ Traffic Detector Roadway Data

     Roadway traffic detectors collecting volume, occupancy and speed data from select roadways located
    in Oregon

    Args:
        jurisdiction_id (Union[Unset, str]):
        location_id (Union[Unset, str]):
        highway_name (Union[Unset, str]):
        milepoint (Union[Unset, str]):
        station_id (Union[Unset, str]):
        station_class (Union[Unset, str]):
        ramp_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TDRoadwayData]
     """


    return (await asyncio_detailed(
        client=client,
jurisdiction_id=jurisdiction_id,
location_id=location_id,
highway_name=highway_name,
milepoint=milepoint,
station_id=station_id,
station_class=station_class,
ramp_id=ramp_id,

    )).parsed
