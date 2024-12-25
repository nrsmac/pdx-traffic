from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rwis_status_v2 import RwisStatusV2
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["StationId"] = station_id

    params["RouteId"] = route_id

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/Rwis/Status",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, RwisStatusV2]]:
    if response.status_code == 200:
        response_200 = RwisStatusV2.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, RwisStatusV2]]:
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
    route_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, RwisStatusV2]]:
    """ RWIS Status V2

     Weather data from automated Weather stations along state highways
    (e.g. Air Temperature, Surface Temperature, wind speed, etc.)
    Note: not all stations can measure all types of weather factors.
    Note: uses RwisStatusNtcip.xml instead of RwisStatus2.xml to produce NTCIP standard values.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RwisStatusV2]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
route_id=route_id,
bounds=bounds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, RwisStatusV2]]:
    """ RWIS Status V2

     Weather data from automated Weather stations along state highways
    (e.g. Air Temperature, Surface Temperature, wind speed, etc.)
    Note: not all stations can measure all types of weather factors.
    Note: uses RwisStatusNtcip.xml instead of RwisStatus2.xml to produce NTCIP standard values.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RwisStatusV2]
     """


    return sync_detailed(
        client=client,
station_id=station_id,
route_id=route_id,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, RwisStatusV2]]:
    """ RWIS Status V2

     Weather data from automated Weather stations along state highways
    (e.g. Air Temperature, Surface Temperature, wind speed, etc.)
    Note: not all stations can measure all types of weather factors.
    Note: uses RwisStatusNtcip.xml instead of RwisStatus2.xml to produce NTCIP standard values.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RwisStatusV2]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
route_id=route_id,
bounds=bounds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, RwisStatusV2]]:
    """ RWIS Status V2

     Weather data from automated Weather stations along state highways
    (e.g. Air Temperature, Surface Temperature, wind speed, etc.)
    Note: not all stations can measure all types of weather factors.
    Note: uses RwisStatusNtcip.xml instead of RwisStatus2.xml to produce NTCIP standard values.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RwisStatusV2]
     """


    return (await asyncio_detailed(
        client=client,
station_id=station_id,
route_id=route_id,
bounds=bounds,

    )).parsed
