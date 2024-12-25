from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rw_end_location import RWEndLocation
  from ..models.rw_start_location import RWStartLocation





T = TypeVar("T", bound="RWLocation")


@_attrs_define
class RWLocation:
    """ Location

        Attributes:
            location_name (Union[Unset, str]): Location Name
            route_id (Union[Unset, str]): Route identifier
            hwy_id (Union[Unset, str]): Highway identifier
            direction (Union[Unset, str]): Direction
            start_location (Union[Unset, RWStartLocation]): Begin Location
            end_location (Union[Unset, RWEndLocation]): End Location
     """

    location_name: Union[Unset, str] = UNSET
    route_id: Union[Unset, str] = UNSET
    hwy_id: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    start_location: Union[Unset, 'RWStartLocation'] = UNSET
    end_location: Union[Unset, 'RWEndLocation'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rw_end_location import RWEndLocation
        from ..models.rw_start_location import RWStartLocation
        location_name = self.location_name

        route_id = self.route_id

        hwy_id = self.hwy_id

        direction = self.direction

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
        if start_location is not UNSET:
            field_dict["start-location"] = start_location
        if end_location is not UNSET:
            field_dict["end-location"] = end_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rw_end_location import RWEndLocation
        from ..models.rw_start_location import RWStartLocation
        d = src_dict.copy()
        location_name = d.pop("location-name", UNSET)

        route_id = d.pop("route-id", UNSET)

        hwy_id = d.pop("hwy-id", UNSET)

        direction = d.pop("direction", UNSET)

        _start_location = d.pop("start-location", UNSET)
        start_location: Union[Unset, RWStartLocation]
        if isinstance(_start_location,  Unset):
            start_location = UNSET
        else:
            start_location = RWStartLocation.from_dict(_start_location)




        _end_location = d.pop("end-location", UNSET)
        end_location: Union[Unset, RWEndLocation]
        if isinstance(_end_location,  Unset):
            end_location = UNSET
        else:
            end_location = RWEndLocation.from_dict(_end_location)




        rw_location = cls(
            location_name=location_name,
            route_id=route_id,
            hwy_id=hwy_id,
            direction=direction,
            start_location=start_location,
            end_location=end_location,
        )


        rw_location.additional_properties = d
        return rw_location

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
