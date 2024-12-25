from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.wz_dx_activities import WZDxActivities
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    subidentifier: Union[Unset, str] = UNSET,
    road_name: Union[Unset, str] = UNSET,
    wz_status: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["subidentifier"] = subidentifier

    params["roadName"] = road_name

    params["wz_status"] = wz_status

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/WZDx/Activities",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, WZDxActivities]]:
    if response.status_code == 200:
        response_200 = WZDxActivities.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, WZDxActivities]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    subidentifier: Union[Unset, str] = UNSET,
    road_name: Union[Unset, str] = UNSET,
    wz_status: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, WZDxActivities]]:
    """ WZDx Activities

     Work zone related activities occurring throughout the State of Oregon formatted according to the
    WZDx standard created by the FHWA and USDOT.

    Args:
        subidentifier (Union[Unset, str]):
        road_name (Union[Unset, str]):
        wz_status (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WZDxActivities]]
     """


    kwargs = _get_kwargs(
        subidentifier=subidentifier,
road_name=road_name,
wz_status=wz_status,
bounds=bounds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    subidentifier: Union[Unset, str] = UNSET,
    road_name: Union[Unset, str] = UNSET,
    wz_status: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, WZDxActivities]]:
    """ WZDx Activities

     Work zone related activities occurring throughout the State of Oregon formatted according to the
    WZDx standard created by the FHWA and USDOT.

    Args:
        subidentifier (Union[Unset, str]):
        road_name (Union[Unset, str]):
        wz_status (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WZDxActivities]
     """


    return sync_detailed(
        client=client,
subidentifier=subidentifier,
road_name=road_name,
wz_status=wz_status,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    subidentifier: Union[Unset, str] = UNSET,
    road_name: Union[Unset, str] = UNSET,
    wz_status: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, WZDxActivities]]:
    """ WZDx Activities

     Work zone related activities occurring throughout the State of Oregon formatted according to the
    WZDx standard created by the FHWA and USDOT.

    Args:
        subidentifier (Union[Unset, str]):
        road_name (Union[Unset, str]):
        wz_status (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WZDxActivities]]
     """


    kwargs = _get_kwargs(
        subidentifier=subidentifier,
road_name=road_name,
wz_status=wz_status,
bounds=bounds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    subidentifier: Union[Unset, str] = UNSET,
    road_name: Union[Unset, str] = UNSET,
    wz_status: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, WZDxActivities]]:
    """ WZDx Activities

     Work zone related activities occurring throughout the State of Oregon formatted according to the
    WZDx standard created by the FHWA and USDOT.

    Args:
        subidentifier (Union[Unset, str]):
        road_name (Union[Unset, str]):
        wz_status (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WZDxActivities]
     """


    return (await asyncio_detailed(
        client=client,
subidentifier=subidentifier,
road_name=road_name,
wz_status=wz_status,
bounds=bounds,

    )).parsed
