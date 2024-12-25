from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="ClsInventoryItem")


@_attrs_define
class ClsInventoryItem:
    """ Class to hold a single bin configuration for a CLS station

        Attributes:
            station_id (Union[Unset, int]): The unique station identifier
            type_ (Union[Unset, str]): Classification of data collected by the station
            bin_number (Union[Unset, int]): The identifier of the bin classification
            bin_value_description (Union[Unset, float]): The classification aggregate value
            configure_time (Union[Unset, datetime.datetime]): The time at which the classfication was configured
     """

    station_id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    bin_number: Union[Unset, int] = UNSET
    bin_value_description: Union[Unset, float] = UNSET
    configure_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        station_id = self.station_id

        type_ = self.type_

        bin_number = self.bin_number

        bin_value_description = self.bin_value_description

        configure_time: Union[Unset, str] = UNSET
        if not isinstance(self.configure_time, Unset):
            configure_time = self.configure_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bin_number is not UNSET:
            field_dict["bin-number"] = bin_number
        if bin_value_description is not UNSET:
            field_dict["bin-value-description"] = bin_value_description
        if configure_time is not UNSET:
            field_dict["configure-time"] = configure_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        type_ = d.pop("type", UNSET)

        bin_number = d.pop("bin-number", UNSET)

        bin_value_description = d.pop("bin-value-description", UNSET)

        _configure_time = d.pop("configure-time", UNSET)
        configure_time: Union[Unset, datetime.datetime]
        if isinstance(_configure_time,  Unset):
            configure_time = UNSET
        else:
            configure_time = isoparse(_configure_time)




        cls_inventory_item = cls(
            station_id=station_id,
            type_=type_,
            bin_number=bin_number,
            bin_value_description=bin_value_description,
            configure_time=configure_time,
        )


        cls_inventory_item.additional_properties = d
        return cls_inventory_item

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
