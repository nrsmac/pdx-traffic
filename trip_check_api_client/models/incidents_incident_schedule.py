from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncidentsIncidentSchedule")


@_attrs_define
class IncidentsIncidentSchedule:
    """ The schedule encapsulates all start and end times for an recurring incident.

        Attributes:
            everyday (Union[Unset, str]):
            monday (Union[Unset, str]):
            tuesday (Union[Unset, str]):
            wednesday (Union[Unset, str]):
            thursday (Union[Unset, str]):
            friday (Union[Unset, str]):
            saturday (Union[Unset, str]):
            sunday (Union[Unset, str]):
     """

    everyday: Union[Unset, str] = UNSET
    monday: Union[Unset, str] = UNSET
    tuesday: Union[Unset, str] = UNSET
    wednesday: Union[Unset, str] = UNSET
    thursday: Union[Unset, str] = UNSET
    friday: Union[Unset, str] = UNSET
    saturday: Union[Unset, str] = UNSET
    sunday: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        everyday = self.everyday

        monday = self.monday

        tuesday = self.tuesday

        wednesday = self.wednesday

        thursday = self.thursday

        friday = self.friday

        saturday = self.saturday

        sunday = self.sunday


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if everyday is not UNSET:
            field_dict["everyday"] = everyday
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        everyday = d.pop("everyday", UNSET)

        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        incidents_incident_schedule = cls(
            everyday=everyday,
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )


        incidents_incident_schedule.additional_properties = d
        return incidents_incident_schedule

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
