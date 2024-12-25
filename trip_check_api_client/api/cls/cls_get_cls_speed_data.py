from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cls_data import ClsData
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    station_id: Union[Unset, str] = UNSET,
    lane: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["StationId"] = station_id

    params["Lane"] = lane

    params["RecordedDate"] = recorded_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Cls/Speed",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ClsData]]:
    if response.status_code == 200:
        response_200 = ClsData.from_dict(response.json())



        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ClsData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    lane: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ClsData]]:
    """ CLS Speed Data

     Speed data aggregated by speed classification for each detector station.
    The Bin Count represents the speed of vehicles that passed the detector
    station in a 20 second period that fall into that particular speed classification.

    Args:
        station_id (Union[Unset, str]):
        lane (Union[Unset, str]):
        recorded_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClsData]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
lane=lane,
recorded_date=recorded_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    lane: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ClsData]]:
    """ CLS Speed Data

     Speed data aggregated by speed classification for each detector station.
    The Bin Count represents the speed of vehicles that passed the detector
    station in a 20 second period that fall into that particular speed classification.

    Args:
        station_id (Union[Unset, str]):
        lane (Union[Unset, str]):
        recorded_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClsData]
     """


    return sync_detailed(
        client=client,
station_id=station_id,
lane=lane,
recorded_date=recorded_date,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    lane: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ClsData]]:
    """ CLS Speed Data

     Speed data aggregated by speed classification for each detector station.
    The Bin Count represents the speed of vehicles that passed the detector
    station in a 20 second period that fall into that particular speed classification.

    Args:
        station_id (Union[Unset, str]):
        lane (Union[Unset, str]):
        recorded_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClsData]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
lane=lane,
recorded_date=recorded_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    lane: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ClsData]]:
    """ CLS Speed Data

     Speed data aggregated by speed classification for each detector station.
    The Bin Count represents the speed of vehicles that passed the detector
    station in a 20 second period that fall into that particular speed classification.

    Args:
        station_id (Union[Unset, str]):
        lane (Union[Unset, str]):
        recorded_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClsData]
     """


    return (await asyncio_detailed(
        client=client,
station_id=station_id,
lane=lane,
recorded_date=recorded_date,

    )).parsed
