from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="OrganizationInfo")


@_attrs_define
class OrganizationInfo:
    """ Organization Information

        Attributes:
            organization_id (Union[Unset, str]): Organization Identifier
            organization_name (Union[Unset, str]): Organization Name
            last_update_time (Union[Unset, datetime.datetime]): Date of last update (UTC)
     """

    organization_id: Union[Unset, str] = UNSET
    organization_name: Union[Unset, str] = UNSET
    last_update_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization_name = self.organization_name

        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_id is not UNSET:
            field_dict["organization-id"] = organization_id
        if organization_name is not UNSET:
            field_dict["organization-name"] = organization_name
        if last_update_time is not UNSET:
            field_dict["last-update-time"] = last_update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_id = d.pop("organization-id", UNSET)

        organization_name = d.pop("organization-name", UNSET)

        _last_update_time = d.pop("last-update-time", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time,  Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)




        organization_info = cls(
            organization_id=organization_id,
            organization_name=organization_name,
            last_update_time=last_update_time,
        )


        organization_info.additional_properties = d
        return organization_info

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
