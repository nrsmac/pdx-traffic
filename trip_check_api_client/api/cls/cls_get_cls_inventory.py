from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cls_inventory import ClsInventory
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    station_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bin_value_desc: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["StationId"] = station_id

    params["Type"] = type_

    params["BinValueDesc"] = bin_value_desc


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Cls/Inventory",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ClsInventory]]:
    if response.status_code == 200:
        response_200 = ClsInventory.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ClsInventory]]:
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
    type_: Union[Unset, str] = UNSET,
    bin_value_desc: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ClsInventory]]:
    """ CLS Inventory

     Vehicle Length and Speed classifications for each Detector Station.
    This data defines what vehicle length values are being used for aggregation.
    The data is collected through web services on Automated Traffic Controllers (ATCs).

    Args:
        station_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bin_value_desc (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClsInventory]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
type_=type_,
bin_value_desc=bin_value_desc,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bin_value_desc: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ClsInventory]]:
    """ CLS Inventory

     Vehicle Length and Speed classifications for each Detector Station.
    This data defines what vehicle length values are being used for aggregation.
    The data is collected through web services on Automated Traffic Controllers (ATCs).

    Args:
        station_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bin_value_desc (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClsInventory]
     """


    return sync_detailed(
        client=client,
station_id=station_id,
type_=type_,
bin_value_desc=bin_value_desc,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bin_value_desc: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ClsInventory]]:
    """ CLS Inventory

     Vehicle Length and Speed classifications for each Detector Station.
    This data defines what vehicle length values are being used for aggregation.
    The data is collected through web services on Automated Traffic Controllers (ATCs).

    Args:
        station_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bin_value_desc (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClsInventory]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
type_=type_,
bin_value_desc=bin_value_desc,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    station_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bin_value_desc: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ClsInventory]]:
    """ CLS Inventory

     Vehicle Length and Speed classifications for each Detector Station.
    This data defines what vehicle length values are being used for aggregation.
    The data is collected through web services on Automated Traffic Controllers (ATCs).

    Args:
        station_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bin_value_desc (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClsInventory]
     """


    return (await asyncio_detailed(
        client=client,
station_id=station_id,
type_=type_,
bin_value_desc=bin_value_desc,

    )).parsed
