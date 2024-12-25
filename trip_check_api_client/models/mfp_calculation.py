from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.mfp_location import MfpLocation





T = TypeVar("T", bound="MfpCalculation")


@_attrs_define
class MfpCalculation:
    """ Parking lot location and percentage information

        Attributes:
            last_update_time (Union[Unset, datetime.datetime]): Last update time of the percentage data
            location (Union[Unset, MfpLocation]): Location data for the parking lot
            percent_full (Union[Unset, int]): Percentage full for the parking lot
            percent_full_message (Union[Unset, str]): String representation of parking lot percentage full
     """

    last_update_time: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, 'MfpLocation'] = UNSET
    percent_full: Union[Unset, int] = UNSET
    percent_full_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.mfp_location import MfpLocation
        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        percent_full = self.percent_full

        percent_full_message = self.percent_full_message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if last_update_time is not UNSET:
            field_dict["last-update-time"] = last_update_time
        if location is not UNSET:
            field_dict["location"] = location
        if percent_full is not UNSET:
            field_dict["percentFull"] = percent_full
        if percent_full_message is not UNSET:
            field_dict["percentFullMessage"] = percent_full_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.mfp_location import MfpLocation
        d = src_dict.copy()
        _last_update_time = d.pop("last-update-time", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time,  Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)




        _location = d.pop("location", UNSET)
        location: Union[Unset, MfpLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = MfpLocation.from_dict(_location)




        percent_full = d.pop("percentFull", UNSET)

        percent_full_message = d.pop("percentFullMessage", UNSET)

        mfp_calculation = cls(
            last_update_time=last_update_time,
            location=location,
            percent_full=percent_full,
            percent_full_message=percent_full_message,
        )


        mfp_calculation.additional_properties = d
        return mfp_calculation

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
