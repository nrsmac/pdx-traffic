from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="TDRDeviceStatusHeader")


@_attrs_define
class TDRDeviceStatusHeader:
    """ Device Status Header

        Attributes:
            ramp_id (Union[Unset, int]): Ramp Id
            device_status (Union[Unset, str]): Device Status
            center_id (Union[Unset, int]): Jurisdiction
            response_plan_id (Union[Unset, int]): Response Plan
            last_comm_time (Union[Unset, datetime.datetime]): Last Communication Time
     """

    ramp_id: Union[Unset, int] = UNSET
    device_status: Union[Unset, str] = UNSET
    center_id: Union[Unset, int] = UNSET
    response_plan_id: Union[Unset, int] = UNSET
    last_comm_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        ramp_id = self.ramp_id

        device_status = self.device_status

        center_id = self.center_id

        response_plan_id = self.response_plan_id

        last_comm_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_comm_time, Unset):
            last_comm_time = self.last_comm_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ramp_id is not UNSET:
            field_dict["ramp-id"] = ramp_id
        if device_status is not UNSET:
            field_dict["device-status"] = device_status
        if center_id is not UNSET:
            field_dict["center-id"] = center_id
        if response_plan_id is not UNSET:
            field_dict["response-plan-id"] = response_plan_id
        if last_comm_time is not UNSET:
            field_dict["last-comm-time"] = last_comm_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ramp_id = d.pop("ramp-id", UNSET)

        device_status = d.pop("device-status", UNSET)

        center_id = d.pop("center-id", UNSET)

        response_plan_id = d.pop("response-plan-id", UNSET)

        _last_comm_time = d.pop("last-comm-time", UNSET)
        last_comm_time: Union[Unset, datetime.datetime]
        if isinstance(_last_comm_time,  Unset):
            last_comm_time = UNSET
        else:
            last_comm_time = isoparse(_last_comm_time)




        tdr_device_status_header = cls(
            ramp_id=ramp_id,
            device_status=device_status,
            center_id=center_id,
            response_plan_id=response_plan_id,
            last_comm_time=last_comm_time,
        )


        tdr_device_status_header.additional_properties = d
        return tdr_device_status_header

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
