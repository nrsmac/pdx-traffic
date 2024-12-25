from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.incidents_incident_location_direction import IncidentsIncidentLocationDirection
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncidentsIncidentLocation")


@_attrs_define
class IncidentsIncidentLocation:
    """ Encapsulates the location information for the incident.

        Attributes:
            location_description (Union[Unset, str]): Specifies the address or other textual description of the incident’s
                location.
            street (Union[Unset, str]): Specifies the name of the street on which the incident is occurring.
            polyline (Union[Unset, str]): Specifies the WGS84 latitude/longitude coordinates that describe the location of
                the incident.
                The decimal value should have at least 6 digits (to ensure accuracy of 0.11m or better).
                For any incident, you must submit at least two coordinates.
            direction (Union[Unset, IncidentsIncidentLocationDirection]): Specifies whether the disruption or closure
                affects one or both sides of the road.
     """

    location_description: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    polyline: Union[Unset, str] = UNSET
    direction: Union[Unset, IncidentsIncidentLocationDirection] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        location_description = self.location_description

        street = self.street

        polyline = self.polyline

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_description is not UNSET:
            field_dict["location_description"] = location_description
        if street is not UNSET:
            field_dict["street"] = street
        if polyline is not UNSET:
            field_dict["polyline"] = polyline
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        location_description = d.pop("location_description", UNSET)

        street = d.pop("street", UNSET)

        polyline = d.pop("polyline", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, IncidentsIncidentLocationDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = IncidentsIncidentLocationDirection(_direction)




        incidents_incident_location = cls(
            location_description=location_description,
            street=street,
            polyline=polyline,
            direction=direction,
        )


        incidents_incident_location.additional_properties = d
        return incidents_incident_location

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
