from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="WZDxStartDates")


@_attrs_define
class WZDxStartDates:
    """ WZDx Events Start Dates

        Attributes:
            start_date_time_est (Union[Unset, datetime.datetime]): The estimated time and date when a work zone starts
     """

    start_date_time_est: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        start_date_time_est: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time_est, Unset):
            start_date_time_est = self.start_date_time_est.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_date_time_est is not UNSET:
            field_dict["StartDateTimeEst"] = start_date_time_est

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_date_time_est = d.pop("StartDateTimeEst", UNSET)
        start_date_time_est: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time_est,  Unset):
            start_date_time_est = UNSET
        else:
            start_date_time_est = isoparse(_start_date_time_est)




        wz_dx_start_dates = cls(
            start_date_time_est=start_date_time_est,
        )


        wz_dx_start_dates.additional_properties = d
        return wz_dx_start_dates

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
