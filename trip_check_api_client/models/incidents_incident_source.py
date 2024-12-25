from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncidentsIncidentSource")


@_attrs_define
class IncidentsIncidentSource:
    """ Encapsulates the elements that specify the source of information for a single incident.

        Attributes:
            reference (Union[Unset, str]): Uses a reference ID to identify the organization that sourced the information.
            name (Union[Unset, str]): Identifies the organization from which the information was sourced, by the
                organization’s name.
            url (Union[Unset, str]): Specifies the URL for the organization from which the information was sourced.
     """

    reference: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        name = self.name

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reference is not UNSET:
            field_dict["reference"] = reference
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        reference = d.pop("reference", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        incidents_incident_source = cls(
            reference=reference,
            name=name,
            url=url,
        )


        incidents_incident_source.additional_properties = d
        return incidents_incident_source

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
