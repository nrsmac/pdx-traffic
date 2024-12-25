from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.incd_start_location import IncdStartLocation
  from ..models.incd_end_location import IncdEndLocation





T = TypeVar("T", bound="IncdLocation")


@_attrs_define
class IncdLocation:
    """ Location

        Attributes:
            location_name (Union[Unset, str]): Location Name
            route_id (Union[Unset, str]): Route identifier
            hwy_id (Union[Unset, str]): Highway identifier
            direction (Union[Unset, str]): Direction of the incident or event
            geometry_wkt_line (Union[Unset, str]): Geometry Well Known Text Line
            start_location (Union[Unset, IncdStartLocation]): Begin Location
            end_location (Union[Unset, IncdEndLocation]): End Location
     """

    location_name: Union[Unset, str] = UNSET
    route_id: Union[Unset, str] = UNSET
    hwy_id: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    geometry_wkt_line: Union[Unset, str] = UNSET
    start_location: Union[Unset, 'IncdStartLocation'] = UNSET
    end_location: Union[Unset, 'IncdEndLocation'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_start_location import IncdStartLocation
        from ..models.incd_end_location import IncdEndLocation
        location_name = self.location_name

        route_id = self.route_id

        hwy_id = self.hwy_id

        direction = self.direction

        geometry_wkt_line = self.geometry_wkt_line

        start_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_location, Unset):
            start_location = self.start_location.to_dict()

        end_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_location, Unset):
            end_location = self.end_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_name is not UNSET:
            field_dict["location-name"] = location_name
        if route_id is not UNSET:
            field_dict["route-id"] = route_id
        if hwy_id is not UNSET:
            field_dict["hwy-id"] = hwy_id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if geometry_wkt_line is not UNSET:
            field_dict["geometry-wkt-line"] = geometry_wkt_line
        if start_location is not UNSET:
            field_dict["start-location"] = start_location
        if end_location is not UNSET:
            field_dict["end-location"] = end_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_start_location import IncdStartLocation
        from ..models.incd_end_location import IncdEndLocation
        d = src_dict.copy()
        location_name = d.pop("location-name", UNSET)

        route_id = d.pop("route-id", UNSET)

        hwy_id = d.pop("hwy-id", UNSET)

        direction = d.pop("direction", UNSET)

        geometry_wkt_line = d.pop("geometry-wkt-line", UNSET)

        _start_location = d.pop("start-location", UNSET)
        start_location: Union[Unset, IncdStartLocation]
        if isinstance(_start_location,  Unset):
            start_location = UNSET
        else:
            start_location = IncdStartLocation.from_dict(_start_location)




        _end_location = d.pop("end-location", UNSET)
        end_location: Union[Unset, IncdEndLocation]
        if isinstance(_end_location,  Unset):
            end_location = UNSET
        else:
            end_location = IncdEndLocation.from_dict(_end_location)




        incd_location = cls(
            location_name=location_name,
            route_id=route_id,
            hwy_id=hwy_id,
            direction=direction,
            geometry_wkt_line=geometry_wkt_line,
            start_location=start_location,
            end_location=end_location,
        )


        incd_location.additional_properties = d
        return incd_location

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
