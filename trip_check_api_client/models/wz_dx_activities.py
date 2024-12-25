from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.wz_dx_activity import WZDxActivity
  from ..models.wz_dx_header import WZDxHeader





T = TypeVar("T", bound="WZDxActivities")


@_attrs_define
class WZDxActivities:
    """ WZDx Activities List

        Attributes:
            header (Union[Unset, WZDxHeader]): This class contains all the WorkZone Activity fields
            activities (Union[Unset, list['WZDxActivity']]): List of Work Zone Activities
     """

    header: Union[Unset, 'WZDxHeader'] = UNSET
    activities: Union[Unset, list['WZDxActivity']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.wz_dx_activity import WZDxActivity
        from ..models.wz_dx_header import WZDxHeader
        header: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        activities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.activities, Unset):
            activities = []
            for activities_item_data in self.activities:
                activities_item = activities_item_data.to_dict()
                activities.append(activities_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if header is not UNSET:
            field_dict["Header"] = header
        if activities is not UNSET:
            field_dict["Activities"] = activities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.wz_dx_activity import WZDxActivity
        from ..models.wz_dx_header import WZDxHeader
        d = src_dict.copy()
        _header = d.pop("Header", UNSET)
        header: Union[Unset, WZDxHeader]
        if isinstance(_header,  Unset):
            header = UNSET
        else:
            header = WZDxHeader.from_dict(_header)




        activities = []
        _activities = d.pop("Activities", UNSET)
        for activities_item_data in (_activities or []):
            activities_item = WZDxActivity.from_dict(activities_item_data)



            activities.append(activities_item)


        wz_dx_activities = cls(
            header=header,
            activities=activities,
        )


        wz_dx_activities.additional_properties = d
        return wz_dx_activities

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
