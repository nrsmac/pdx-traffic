from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.incidents_incident import IncidentsIncident





T = TypeVar("T", bound="Incidents")


@_attrs_define
class Incidents:
    """ Incident information
    Waze accepts feed data for both real-time or planned traffic incidents,
    including hazards on the road, construction, and more.Incidents don’t
    affect real-time navigation, they only alert drivers.
    <a href="https://developers.google.com/waze/data-feed/incident-information" />

        Attributes:
            timestamp (Union[Unset, datetime.datetime]): Specifies the creation time of the feed.
            no_namespace_schema_location (Union[Unset, str]):
            incident (Union[Unset, list['IncidentsIncident']]): List of incidents
     """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    no_namespace_schema_location: Union[Unset, str] = UNSET
    incident: Union[Unset, list['IncidentsIncident']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incidents_incident import IncidentsIncident
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        no_namespace_schema_location = self.no_namespace_schema_location

        incident: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.incident, Unset):
            incident = []
            for incident_item_data in self.incident:
                incident_item = incident_item_data.to_dict()
                incident.append(incident_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if no_namespace_schema_location is not UNSET:
            field_dict["noNamespaceSchemaLocation"] = no_namespace_schema_location
        if incident is not UNSET:
            field_dict["incident"] = incident

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incidents_incident import IncidentsIncident
        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        no_namespace_schema_location = d.pop("noNamespaceSchemaLocation", UNSET)

        incident = []
        _incident = d.pop("incident", UNSET)
        for incident_item_data in (_incident or []):
            incident_item = IncidentsIncident.from_dict(incident_item_data)



            incident.append(incident_item)


        incidents = cls(
            timestamp=timestamp,
            no_namespace_schema_location=no_namespace_schema_location,
            incident=incident,
        )


        incidents.additional_properties = d
        return incidents

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
