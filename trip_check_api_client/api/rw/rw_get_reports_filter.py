from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rw_reports import RWReports
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    restriction_id: Union[Unset, str] = UNSET,
    road_cond_id: Union[Unset, str] = UNSET,
    weather_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["StationId"] = station_id

    params["RouteId"] = route_id

    params["RestrictionId"] = restriction_id

    params["RoadCondId"] = road_cond_id

    params["WeatherId"] = weather_id

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/RW/Reports",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, RWReports]]:
    if response.status_code == 200:
        response_200 = RWReports.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, RWReports]]:
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
    restriction_id: Union[Unset, str] = UNSET,
    road_cond_id: Union[Unset, str] = UNSET,
    weather_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, RWReports]]:
    """ Road and Weather Reports

     Current road conditions as reported by ODOT crews. This includes weather observations and tire chain
    restrictions.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        restriction_id (Union[Unset, str]):
        road_cond_id (Union[Unset, str]):
        weather_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RWReports]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
route_id=route_id,
restriction_id=restriction_id,
road_cond_id=road_cond_id,
weather_id=weather_id,
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
    restriction_id: Union[Unset, str] = UNSET,
    road_cond_id: Union[Unset, str] = UNSET,
    weather_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, RWReports]]:
    """ Road and Weather Reports

     Current road conditions as reported by ODOT crews. This includes weather observations and tire chain
    restrictions.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        restriction_id (Union[Unset, str]):
        road_cond_id (Union[Unset, str]):
        weather_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RWReports]
     """


    return sync_detailed(
        client=client,
station_id=station_id,
route_id=route_id,
restriction_id=restriction_id,
road_cond_id=road_cond_id,
weather_id=weather_id,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    restriction_id: Union[Unset, str] = UNSET,
    road_cond_id: Union[Unset, str] = UNSET,
    weather_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, RWReports]]:
    """ Road and Weather Reports

     Current road conditions as reported by ODOT crews. This includes weather observations and tire chain
    restrictions.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        restriction_id (Union[Unset, str]):
        road_cond_id (Union[Unset, str]):
        weather_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RWReports]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
route_id=route_id,
restriction_id=restriction_id,
road_cond_id=road_cond_id,
weather_id=weather_id,
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
    restriction_id: Union[Unset, str] = UNSET,
    road_cond_id: Union[Unset, str] = UNSET,
    weather_id: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, RWReports]]:
    """ Road and Weather Reports

     Current road conditions as reported by ODOT crews. This includes weather observations and tire chain
    restrictions.

    Args:
        station_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        restriction_id (Union[Unset, str]):
        road_cond_id (Union[Unset, str]):
        weather_id (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RWReports]
     """


    return (await asyncio_detailed(
        client=client,
station_id=station_id,
route_id=route_id,
restriction_id=restriction_id,
road_cond_id=road_cond_id,
weather_id=weather_id,
bounds=bounds,

    )).parsed
