from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncdIFTFile")


@_attrs_define
class IncdIFTFile:
    """ IFT File

        Attributes:
            url (Union[Unset, str]): URL
            file_description (Union[Unset, str]): File Description
     """

    url: Union[Unset, str] = UNSET
    file_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        url = self.url

        file_description = self.file_description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if file_description is not UNSET:
            field_dict["file-description"] = file_description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        file_description = d.pop("file-description", UNSET)

        incd_ift_file = cls(
            url=url,
            file_description=file_description,
        )


        incd_ift_file.additional_properties = d
        return incd_ift_file

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
