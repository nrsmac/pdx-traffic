from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RwisStatusSiteSensor")


@_attrs_define
class RwisStatusSiteSensor:
    """ RWIS Status Site Sensor info

        Attributes:
            sensor_id (Union[Unset, int]): RWIS sensor type
            surface_temperature (Union[Unset, int]): Surface temperature
     """

    sensor_id: Union[Unset, int] = UNSET
    surface_temperature: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        sensor_id = self.sensor_id

        surface_temperature = self.surface_temperature


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sensor_id is not UNSET:
            field_dict["sensor-id"] = sensor_id
        if surface_temperature is not UNSET:
            field_dict["surface-temperature"] = surface_temperature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sensor_id = d.pop("sensor-id", UNSET)

        surface_temperature = d.pop("surface-temperature", UNSET)

        rwis_status_site_sensor = cls(
            sensor_id=sensor_id,
            surface_temperature=surface_temperature,
        )


        rwis_status_site_sensor.additional_properties = d
        return rwis_status_site_sensor

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
