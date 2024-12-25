from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="WeatherCondition")


@_attrs_define
class WeatherCondition:
    """ List of all weather condition identifiers and descriptions

        Attributes:
            weather_id (Union[Unset, int]): Id of weather condition
            weather_desc (Union[Unset, str]): Description of weather condition
     """

    weather_id: Union[Unset, int] = UNSET
    weather_desc: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        weather_id = self.weather_id

        weather_desc = self.weather_desc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if weather_id is not UNSET:
            field_dict["weather-id"] = weather_id
        if weather_desc is not UNSET:
            field_dict["weather-desc"] = weather_desc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        weather_id = d.pop("weather-id", UNSET)

        weather_desc = d.pop("weather-desc", UNSET)

        weather_condition = cls(
            weather_id=weather_id,
            weather_desc=weather_desc,
        )


        weather_condition.additional_properties = d
        return weather_condition

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
