from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.local_events import LocalEvents
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    type_id: Union[Unset, str] = UNSET,
    impact_id: Union[Unset, str] = UNSET,
    source_agency: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["Id"] = id

    params["TypeId"] = type_id

    params["ImpactId"] = impact_id

    params["SourceAgency"] = source_agency

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Tle/Events",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, LocalEvents]]:
    if response.status_code == 200:
        response_200 = LocalEvents.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, LocalEvents]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    type_id: Union[Unset, str] = UNSET,
    impact_id: Union[Unset, str] = UNSET,
    source_agency: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, LocalEvents]]:
    """ Local Incidents

     Events occurring on local and county roads as reported by non-ODOT government agencies (ex.,
    Washington County, City of Eugene Public Works).

    Args:
        id (Union[Unset, str]):
        type_id (Union[Unset, str]):
        impact_id (Union[Unset, str]):
        source_agency (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LocalEvents]]
     """


    kwargs = _get_kwargs(
        id=id,
type_id=type_id,
impact_id=impact_id,
source_agency=source_agency,
bounds=bounds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    type_id: Union[Unset, str] = UNSET,
    impact_id: Union[Unset, str] = UNSET,
    source_agency: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, LocalEvents]]:
    """ Local Incidents

     Events occurring on local and county roads as reported by non-ODOT government agencies (ex.,
    Washington County, City of Eugene Public Works).

    Args:
        id (Union[Unset, str]):
        type_id (Union[Unset, str]):
        impact_id (Union[Unset, str]):
        source_agency (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LocalEvents]
     """


    return sync_detailed(
        client=client,
id=id,
type_id=type_id,
impact_id=impact_id,
source_agency=source_agency,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    type_id: Union[Unset, str] = UNSET,
    impact_id: Union[Unset, str] = UNSET,
    source_agency: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, LocalEvents]]:
    """ Local Incidents

     Events occurring on local and county roads as reported by non-ODOT government agencies (ex.,
    Washington County, City of Eugene Public Works).

    Args:
        id (Union[Unset, str]):
        type_id (Union[Unset, str]):
        impact_id (Union[Unset, str]):
        source_agency (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LocalEvents]]
     """


    kwargs = _get_kwargs(
        id=id,
type_id=type_id,
impact_id=impact_id,
source_agency=source_agency,
bounds=bounds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    type_id: Union[Unset, str] = UNSET,
    impact_id: Union[Unset, str] = UNSET,
    source_agency: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, LocalEvents]]:
    """ Local Incidents

     Events occurring on local and county roads as reported by non-ODOT government agencies (ex.,
    Washington County, City of Eugene Public Works).

    Args:
        id (Union[Unset, str]):
        type_id (Union[Unset, str]):
        impact_id (Union[Unset, str]):
        source_agency (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LocalEvents]
     """


    return (await asyncio_detailed(
        client=client,
id=id,
type_id=type_id,
impact_id=impact_id,
source_agency=source_agency,
bounds=bounds,

    )).parsed
