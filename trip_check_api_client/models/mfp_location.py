from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="MfpLocation")


@_attrs_define
class MfpLocation:
    """ Location data for the parking lot

        Attributes:
            location_name (Union[Unset, str]): The location name of the parking lot.
            latitude (Union[Unset, float]): The latitude value of the coordinates of the parking lot's location.
            longitude (Union[Unset, float]): The longitude value of the coordinates of the parking lot's location.
     """

    location_name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        location_name = self.location_name

        latitude = self.latitude

        longitude = self.longitude


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        location_name = d.pop("locationName", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        mfp_location = cls(
            location_name=location_name,
            latitude=latitude,
            longitude=longitude,
        )


        mfp_location.additional_properties = d
        return mfp_location

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
