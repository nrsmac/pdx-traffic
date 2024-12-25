from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.incidents import Incidents
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    incident_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["IncidentId"] = incident_id

    params["Type"] = type_

    params["Bounds"] = bounds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Tle/WazeSpec",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Incidents]]:
    if response.status_code == 200:
        response_200 = Incidents.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Incidents]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, Incidents]]:
    """ Local Incidents - Waze Format

     Events occurring on local and county roads as reported by non-ODOT government agencies
    and formatted to the Waze CIFS V2 standard… (ex., Washington County, City of Eugene Public Works)

    Args:
        incident_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Incidents]]
     """


    kwargs = _get_kwargs(
        incident_id=incident_id,
type_=type_,
bounds=bounds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, Incidents]]:
    """ Local Incidents - Waze Format

     Events occurring on local and county roads as reported by non-ODOT government agencies
    and formatted to the Waze CIFS V2 standard… (ex., Washington County, City of Eugene Public Works)

    Args:
        incident_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Incidents]
     """


    return sync_detailed(
        client=client,
incident_id=incident_id,
type_=type_,
bounds=bounds,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Response[Union[Any, Incidents]]:
    """ Local Incidents - Waze Format

     Events occurring on local and county roads as reported by non-ODOT government agencies
    and formatted to the Waze CIFS V2 standard… (ex., Washington County, City of Eugene Public Works)

    Args:
        incident_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Incidents]]
     """


    kwargs = _get_kwargs(
        incident_id=incident_id,
type_=type_,
bounds=bounds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    incident_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    bounds: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, Incidents]]:
    """ Local Incidents - Waze Format

     Events occurring on local and county roads as reported by non-ODOT government agencies
    and formatted to the Waze CIFS V2 standard… (ex., Washington County, City of Eugene Public Works)

    Args:
        incident_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        bounds (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Incidents]
     """


    return (await asyncio_detailed(
        client=client,
incident_id=incident_id,
type_=type_,
bounds=bounds,

    )).parsed
