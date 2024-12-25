from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.dms_status_item import DmsStatusItem
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="DmsStatus")


@_attrs_define
class DmsStatus:
    """ DMS Status List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            dms_items (Union[Unset, list['DmsStatusItem']]): List of DMS Status Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    dms_items: Union[Unset, list['DmsStatusItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.dms_status_item import DmsStatusItem
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        dms_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dms_items, Unset):
            dms_items = []
            for dms_items_item_data in self.dms_items:
                dms_items_item = dms_items_item_data.to_dict()
                dms_items.append(dms_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if dms_items is not UNSET:
            field_dict["dmsItems"] = dms_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dms_status_item import DmsStatusItem
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        dms_items = []
        _dms_items = d.pop("dmsItems", UNSET)
        for dms_items_item_data in (_dms_items or []):
            dms_items_item = DmsStatusItem.from_dict(dms_items_item_data)



            dms_items.append(dms_items_item)


        dms_status = cls(
            organization_information=organization_information,
            dms_items=dms_items,
        )


        dms_status.additional_properties = d
        return dms_status

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
