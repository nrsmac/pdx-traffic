from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="Routes")


@_attrs_define
class Routes:
    """ Route Name List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            location_list (Union[Unset, list[str]]): List of Routes
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    location_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        location_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.location_list, Unset):
            location_list = self.location_list




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if location_list is not UNSET:
            field_dict["location-list"] = location_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        location_list = cast(list[str], d.pop("location-list", UNSET))


        routes = cls(
            organization_information=organization_information,
            location_list=location_list,
        )


        routes.additional_properties = d
        return routes

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
