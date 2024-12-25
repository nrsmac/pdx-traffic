from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.cctv_inventory_item import CctvInventoryItem





T = TypeVar("T", bound="CctvInventory")


@_attrs_define
class CctvInventory:
    """ CCTV Inventory List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            cctv_inventory_request (Union[Unset, list['CctvInventoryItem']]): List of CCTV Inventory Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    cctv_inventory_request: Union[Unset, list['CctvInventoryItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.cctv_inventory_item import CctvInventoryItem
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        cctv_inventory_request: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cctv_inventory_request, Unset):
            cctv_inventory_request = []
            for cctv_inventory_request_item_data in self.cctv_inventory_request:
                cctv_inventory_request_item = cctv_inventory_request_item_data.to_dict()
                cctv_inventory_request.append(cctv_inventory_request_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if cctv_inventory_request is not UNSET:
            field_dict["CCTVInventoryRequest"] = cctv_inventory_request

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.cctv_inventory_item import CctvInventoryItem
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        cctv_inventory_request = []
        _cctv_inventory_request = d.pop("CCTVInventoryRequest", UNSET)
        for cctv_inventory_request_item_data in (_cctv_inventory_request or []):
            cctv_inventory_request_item = CctvInventoryItem.from_dict(cctv_inventory_request_item_data)



            cctv_inventory_request.append(cctv_inventory_request_item)


        cctv_inventory = cls(
            organization_information=organization_information,
            cctv_inventory_request=cctv_inventory_request,
        )


        cctv_inventory.additional_properties = d
        return cctv_inventory

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
