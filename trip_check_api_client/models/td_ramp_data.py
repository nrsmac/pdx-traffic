from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.td_ramp_meter_status_item import TDRampMeterStatusItem
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="TDRampData")


@_attrs_define
class TDRampData:
    """ Traffic Detector Ramp Data

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            ramp_meter_status_items (Union[Unset, list['TDRampMeterStatusItem']]): List of Ramp Meter Status Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    ramp_meter_status_items: Union[Unset, list['TDRampMeterStatusItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.td_ramp_meter_status_item import TDRampMeterStatusItem
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        ramp_meter_status_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ramp_meter_status_items, Unset):
            ramp_meter_status_items = []
            for ramp_meter_status_items_item_data in self.ramp_meter_status_items:
                ramp_meter_status_items_item = ramp_meter_status_items_item_data.to_dict()
                ramp_meter_status_items.append(ramp_meter_status_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if ramp_meter_status_items is not UNSET:
            field_dict["ramp-meter-status-items"] = ramp_meter_status_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.td_ramp_meter_status_item import TDRampMeterStatusItem
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        ramp_meter_status_items = []
        _ramp_meter_status_items = d.pop("ramp-meter-status-items", UNSET)
        for ramp_meter_status_items_item_data in (_ramp_meter_status_items or []):
            ramp_meter_status_items_item = TDRampMeterStatusItem.from_dict(ramp_meter_status_items_item_data)



            ramp_meter_status_items.append(ramp_meter_status_items_item)


        td_ramp_data = cls(
            organization_information=organization_information,
            ramp_meter_status_items=ramp_meter_status_items,
        )


        td_ramp_data.additional_properties = d
        return td_ramp_data

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
