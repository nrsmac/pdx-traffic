from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.incd_event_type import IncdEventType
  from ..models.incd_event_subtype import IncdEventSubtype





T = TypeVar("T", bound="IncidentMetadataItems")


@_attrs_define
class IncidentMetadataItems:
    """ Class to hold the arrays of different incident metadata items.

        Attributes:
            event_types (Union[Unset, list['IncdEventType']]): list of Event Types
            event_subtypes (Union[Unset, list['IncdEventSubtype']]): List of Event Subtypes
     """

    event_types: Union[Unset, list['IncdEventType']] = UNSET
    event_subtypes: Union[Unset, list['IncdEventSubtype']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_event_type import IncdEventType
        from ..models.incd_event_subtype import IncdEventSubtype
        event_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.to_dict()
                event_types.append(event_types_item)



        event_subtypes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_subtypes, Unset):
            event_subtypes = []
            for event_subtypes_item_data in self.event_subtypes:
                event_subtypes_item = event_subtypes_item_data.to_dict()
                event_subtypes.append(event_subtypes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if event_types is not UNSET:
            field_dict["event-types"] = event_types
        if event_subtypes is not UNSET:
            field_dict["event-subtypes"] = event_subtypes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_event_type import IncdEventType
        from ..models.incd_event_subtype import IncdEventSubtype
        d = src_dict.copy()
        event_types = []
        _event_types = d.pop("event-types", UNSET)
        for event_types_item_data in (_event_types or []):
            event_types_item = IncdEventType.from_dict(event_types_item_data)



            event_types.append(event_types_item)


        event_subtypes = []
        _event_subtypes = d.pop("event-subtypes", UNSET)
        for event_subtypes_item_data in (_event_subtypes or []):
            event_subtypes_item = IncdEventSubtype.from_dict(event_subtypes_item_data)



            event_subtypes.append(event_subtypes_item)


        incident_metadata_items = cls(
            event_types=event_types,
            event_subtypes=event_subtypes,
        )


        incident_metadata_items.additional_properties = d
        return incident_metadata_items

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
