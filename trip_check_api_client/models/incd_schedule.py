from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.incd_project_schedule import IncdProjectSchedule





T = TypeVar("T", bound="IncdSchedule")


@_attrs_define
class IncdSchedule:
    """ Response Schedule

        Attributes:
            project_schedule (Union[Unset, IncdProjectSchedule]): Response Project Schedule
     """

    project_schedule: Union[Unset, 'IncdProjectSchedule'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_project_schedule import IncdProjectSchedule
        project_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.project_schedule, Unset):
            project_schedule = self.project_schedule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if project_schedule is not UNSET:
            field_dict["project-schedule"] = project_schedule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_project_schedule import IncdProjectSchedule
        d = src_dict.copy()
        _project_schedule = d.pop("project-schedule", UNSET)
        project_schedule: Union[Unset, IncdProjectSchedule]
        if isinstance(_project_schedule,  Unset):
            project_schedule = UNSET
        else:
            project_schedule = IncdProjectSchedule.from_dict(_project_schedule)




        incd_schedule = cls(
            project_schedule=project_schedule,
        )


        incd_schedule.additional_properties = d
        return incd_schedule

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
