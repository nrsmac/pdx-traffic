from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="IncdProjectSchedule")


@_attrs_define
class IncdProjectSchedule:
    """ Response Project Schedule

        Attributes:
            start_date_time (Union[Unset, datetime.datetime]): Start DateTime
            end_date_time (Union[Unset, datetime.datetime]): End DateTime
     """

    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_date_time is not UNSET:
            field_dict["start-date-time"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["end-date-time"] = end_date_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_date_time = d.pop("start-date-time", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time,  Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)




        _end_date_time = d.pop("end-date-time", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time,  Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)




        incd_project_schedule = cls(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
        )


        incd_project_schedule.additional_properties = d
        return incd_project_schedule

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
