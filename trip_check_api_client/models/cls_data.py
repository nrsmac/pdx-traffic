from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.cls_data_item import ClsDataItem





T = TypeVar("T", bound="ClsData")


@_attrs_define
class ClsData:
    """ CLS Bin Data (Length and Speed) output class

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            cls_inventory (Union[Unset, list['ClsDataItem']]): Array of station-bin readings
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    cls_inventory: Union[Unset, list['ClsDataItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.cls_data_item import ClsDataItem
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        cls_inventory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cls_inventory, Unset):
            cls_inventory = []
            for cls_inventory_item_data in self.cls_inventory:
                cls_inventory_item = cls_inventory_item_data.to_dict()
                cls_inventory.append(cls_inventory_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if cls_inventory is not UNSET:
            field_dict["CLS-inventory"] = cls_inventory

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.cls_data_item import ClsDataItem
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        cls_inventory = []
        _cls_inventory = d.pop("CLS-inventory", UNSET)
        for cls_inventory_item_data in (_cls_inventory or []):
            cls_inventory_item = ClsDataItem.from_dict(cls_inventory_item_data)



            cls_inventory.append(cls_inventory_item)


        cls_data = cls(
            organization_information=organization_information,
            cls_inventory=cls_inventory,
        )


        cls_data.additional_properties = d
        return cls_data

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
