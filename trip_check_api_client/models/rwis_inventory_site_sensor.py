from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RwisInventorySiteSensor")


@_attrs_define
class RwisInventorySiteSensor:
    """ RWIS sensor list

        Attributes:
            device_id (Union[Unset, int]): Device Id
            device_name (Union[Unset, str]): Device Name
            device_description (Union[Unset, str]): Device Name
     """

    device_id: Union[Unset, int] = UNSET
    device_name: Union[Unset, str] = UNSET
    device_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        device_description = self.device_description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_id is not UNSET:
            field_dict["device-id"] = device_id
        if device_name is not UNSET:
            field_dict["device-name"] = device_name
        if device_description is not UNSET:
            field_dict["device-description"] = device_description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device-id", UNSET)

        device_name = d.pop("device-name", UNSET)

        device_description = d.pop("device-description", UNSET)

        rwis_inventory_site_sensor = cls(
            device_id=device_id,
            device_name=device_name,
            device_description=device_description,
        )


        rwis_inventory_site_sensor.additional_properties = d
        return rwis_inventory_site_sensor

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
