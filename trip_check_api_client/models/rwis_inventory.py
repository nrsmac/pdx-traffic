from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_inventory_site_information import RwisInventorySiteInformation
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="RwisInventory")


@_attrs_define
class RwisInventory:
    """ RWIS Inventory List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            ess_site_list (Union[Unset, list['RwisInventorySiteInformation']]): List of RWIS Inventory Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    ess_site_list: Union[Unset, list['RwisInventorySiteInformation']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_inventory_site_information import RwisInventorySiteInformation
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        ess_site_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ess_site_list, Unset):
            ess_site_list = []
            for ess_site_list_item_data in self.ess_site_list:
                ess_site_list_item = ess_site_list_item_data.to_dict()
                ess_site_list.append(ess_site_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if ess_site_list is not UNSET:
            field_dict["ess-site-list"] = ess_site_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_inventory_site_information import RwisInventorySiteInformation
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        ess_site_list = []
        _ess_site_list = d.pop("ess-site-list", UNSET)
        for ess_site_list_item_data in (_ess_site_list or []):
            ess_site_list_item = RwisInventorySiteInformation.from_dict(ess_site_list_item_data)



            ess_site_list.append(ess_site_list_item)


        rwis_inventory = cls(
            organization_information=organization_information,
            ess_site_list=ess_site_list,
        )


        rwis_inventory.additional_properties = d
        return rwis_inventory

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
