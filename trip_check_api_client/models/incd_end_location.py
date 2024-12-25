from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncdEndLocation")


@_attrs_define
class IncdEndLocation:
    """ End Location

        Attributes:
            location_desc (Union[Unset, str]): End location
            end_lat (Union[Unset, float]): End geographic latitude
            end_long (Union[Unset, float]): End geographic longitude
            end_milepost (Union[Unset, float]): End milepost
            end_point_geometry_wkt (Union[Unset, str]): End Point Geometry Well Known Text
     """

    location_desc: Union[Unset, str] = UNSET
    end_lat: Union[Unset, float] = UNSET
    end_long: Union[Unset, float] = UNSET
    end_milepost: Union[Unset, float] = UNSET
    end_point_geometry_wkt: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        location_desc = self.location_desc

        end_lat = self.end_lat

        end_long = self.end_long

        end_milepost = self.end_milepost

        end_point_geometry_wkt = self.end_point_geometry_wkt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_desc is not UNSET:
            field_dict["location-desc"] = location_desc
        if end_lat is not UNSET:
            field_dict["end-lat"] = end_lat
        if end_long is not UNSET:
            field_dict["end-long"] = end_long
        if end_milepost is not UNSET:
            field_dict["end-milepost"] = end_milepost
        if end_point_geometry_wkt is not UNSET:
            field_dict["end-point-geometry-wkt"] = end_point_geometry_wkt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        location_desc = d.pop("location-desc", UNSET)

        end_lat = d.pop("end-lat", UNSET)

        end_long = d.pop("end-long", UNSET)

        end_milepost = d.pop("end-milepost", UNSET)

        end_point_geometry_wkt = d.pop("end-point-geometry-wkt", UNSET)

        incd_end_location = cls(
            location_desc=location_desc,
            end_lat=end_lat,
            end_long=end_long,
            end_milepost=end_milepost,
            end_point_geometry_wkt=end_point_geometry_wkt,
        )


        incd_end_location.additional_properties = d
        return incd_end_location

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
