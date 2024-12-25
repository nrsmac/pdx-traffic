from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.cls_inventory_item import ClsInventoryItem
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="ClsInventory")


@_attrs_define
class ClsInventory:
    """ CLS Inventory output class

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            cls_inventory_items (Union[Unset, list['ClsInventoryItem']]): Array of CLS station-bin details
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    cls_inventory_items: Union[Unset, list['ClsInventoryItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.cls_inventory_item import ClsInventoryItem
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        cls_inventory_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cls_inventory_items, Unset):
            cls_inventory_items = []
            for cls_inventory_items_item_data in self.cls_inventory_items:
                cls_inventory_items_item = cls_inventory_items_item_data.to_dict()
                cls_inventory_items.append(cls_inventory_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if cls_inventory_items is not UNSET:
            field_dict["cls-inventory-items"] = cls_inventory_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cls_inventory_item import ClsInventoryItem
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        cls_inventory_items = []
        _cls_inventory_items = d.pop("cls-inventory-items", UNSET)
        for cls_inventory_items_item_data in (_cls_inventory_items or []):
            cls_inventory_items_item = ClsInventoryItem.from_dict(cls_inventory_items_item_data)



            cls_inventory_items.append(cls_inventory_items_item)


        cls_inventory = cls(
            organization_information=organization_information,
            cls_inventory_items=cls_inventory_items,
        )


        cls_inventory.additional_properties = d
        return cls_inventory

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
