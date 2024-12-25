from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.dms_inventory_item import DmsInventoryItem
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="DmsInventory")


@_attrs_define
class DmsInventory:
    """ DMS Inventory List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            dms_inventory_items (Union[Unset, list['DmsInventoryItem']]): List of DMS Inventory Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    dms_inventory_items: Union[Unset, list['DmsInventoryItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.dms_inventory_item import DmsInventoryItem
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        dms_inventory_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dms_inventory_items, Unset):
            dms_inventory_items = []
            for dms_inventory_items_item_data in self.dms_inventory_items:
                dms_inventory_items_item = dms_inventory_items_item_data.to_dict()
                dms_inventory_items.append(dms_inventory_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if dms_inventory_items is not UNSET:
            field_dict["dms-inventory-items"] = dms_inventory_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dms_inventory_item import DmsInventoryItem
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        dms_inventory_items = []
        _dms_inventory_items = d.pop("dms-inventory-items", UNSET)
        for dms_inventory_items_item_data in (_dms_inventory_items or []):
            dms_inventory_items_item = DmsInventoryItem.from_dict(dms_inventory_items_item_data)



            dms_inventory_items.append(dms_inventory_items_item)


        dms_inventory = cls(
            organization_information=organization_information,
            dms_inventory_items=dms_inventory_items,
        )


        dms_inventory.additional_properties = d
        return dms_inventory

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
