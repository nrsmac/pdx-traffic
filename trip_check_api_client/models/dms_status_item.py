from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.dms_current_message import DmsCurrentMessage





T = TypeVar("T", bound="DmsStatusItem")


@_attrs_define
class DmsStatusItem:
    """ DMS Status Item

        Attributes:
            device_id (Union[Unset, int]): The unique device identifier
            dms_device_status (Union[Unset, str]): Device status
            tocs_event_id (Union[Unset, str]): TOCS Event Id
            dms_current_message (Union[Unset, DmsCurrentMessage]): Current message on the sign
     """

    device_id: Union[Unset, int] = UNSET
    dms_device_status: Union[Unset, str] = UNSET
    tocs_event_id: Union[Unset, str] = UNSET
    dms_current_message: Union[Unset, 'DmsCurrentMessage'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.dms_current_message import DmsCurrentMessage
        device_id = self.device_id

        dms_device_status = self.dms_device_status

        tocs_event_id = self.tocs_event_id

        dms_current_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dms_current_message, Unset):
            dms_current_message = self.dms_current_message.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_id is not UNSET:
            field_dict["device-id"] = device_id
        if dms_device_status is not UNSET:
            field_dict["dms-device-status"] = dms_device_status
        if tocs_event_id is not UNSET:
            field_dict["tocsEventId"] = tocs_event_id
        if dms_current_message is not UNSET:
            field_dict["dmsCurrentMessage"] = dms_current_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dms_current_message import DmsCurrentMessage
        d = src_dict.copy()
        device_id = d.pop("device-id", UNSET)

        dms_device_status = d.pop("dms-device-status", UNSET)

        tocs_event_id = d.pop("tocsEventId", UNSET)

        _dms_current_message = d.pop("dmsCurrentMessage", UNSET)
        dms_current_message: Union[Unset, DmsCurrentMessage]
        if isinstance(_dms_current_message,  Unset):
            dms_current_message = UNSET
        else:
            dms_current_message = DmsCurrentMessage.from_dict(_dms_current_message)




        dms_status_item = cls(
            device_id=device_id,
            dms_device_status=dms_device_status,
            tocs_event_id=tocs_event_id,
            dms_current_message=dms_current_message,
        )


        dms_status_item.additional_properties = d
        return dms_status_item

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
