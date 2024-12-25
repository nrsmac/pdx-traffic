from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="ClsDataItem")


@_attrs_define
class ClsDataItem:
    """ Class to hold a single station-bin reading

        Attributes:
            station_id (Union[Unset, int]): The unique station identifier
            lane (Union[Unset, int]): The lane number this reading is from
            bin_number (Union[Unset, int]): The identifier of the bin classification
            bin_count (Union[Unset, int]): Number of vehicles matching the classification during the collection cycle
            recorded_date (Union[Unset, datetime.datetime]): The date and time this data was recorded
     """

    station_id: Union[Unset, int] = UNSET
    lane: Union[Unset, int] = UNSET
    bin_number: Union[Unset, int] = UNSET
    bin_count: Union[Unset, int] = UNSET
    recorded_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        station_id = self.station_id

        lane = self.lane

        bin_number = self.bin_number

        bin_count = self.bin_count

        recorded_date: Union[Unset, str] = UNSET
        if not isinstance(self.recorded_date, Unset):
            recorded_date = self.recorded_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if lane is not UNSET:
            field_dict["lane"] = lane
        if bin_number is not UNSET:
            field_dict["bin-number"] = bin_number
        if bin_count is not UNSET:
            field_dict["bin-count"] = bin_count
        if recorded_date is not UNSET:
            field_dict["recorded-date"] = recorded_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        lane = d.pop("lane", UNSET)

        bin_number = d.pop("bin-number", UNSET)

        bin_count = d.pop("bin-count", UNSET)

        _recorded_date = d.pop("recorded-date", UNSET)
        recorded_date: Union[Unset, datetime.datetime]
        if isinstance(_recorded_date,  Unset):
            recorded_date = UNSET
        else:
            recorded_date = isoparse(_recorded_date)




        cls_data_item = cls(
            station_id=station_id,
            lane=lane,
            bin_number=bin_number,
            bin_count=bin_count,
            recorded_date=recorded_date,
        )


        cls_data_item.additional_properties = d
        return cls_data_item

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
