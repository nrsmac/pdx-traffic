from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dms_inventory import DmsInventory
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    device_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["DeviceId"] = device_id

    params["RouteId"] = route_id

    params["Class"] = class_

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Dms/Inventory",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DmsInventory]]:
    if response.status_code == 200:
        response_200 = DmsInventory.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DmsInventory]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, DmsInventory]]:
    """ DMS Inventory

     Name and Location of each Dynamic Message Sign on state highways or controlled by ODOT.

    Args:
        device_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        class_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DmsInventory]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
route_id=route_id,
class_=class_,
bounds=bounds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, DmsInventory]]:
    """ DMS Inventory

     Name and Location of each Dynamic Message Sign on state highways or controlled by ODOT.

    Args:
        device_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        class_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DmsInventory]
     """


    return sync_detailed(
        client=client,
device_id=device_id,
route_id=route_id,
class_=class_,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, DmsInventory]]:
    """ DMS Inventory

     Name and Location of each Dynamic Message Sign on state highways or controlled by ODOT.

    Args:
        device_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        class_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DmsInventory]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
route_id=route_id,
class_=class_,
bounds=bounds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    route_id: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, DmsInventory]]:
    """ DMS Inventory

     Name and Location of each Dynamic Message Sign on state highways or controlled by ODOT.

    Args:
        device_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        class_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DmsInventory]
     """


    return (await asyncio_detailed(
        client=client,
device_id=device_id,
route_id=route_id,
class_=class_,
bounds=bounds,

    )).parsed