from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rw_items import RWItems
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="RWMetadata")


@_attrs_define
class RWMetadata:
    """ Road Weather Metadata

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            road_weather_items (Union[Unset, RWItems]): Class to hold the arrays of different road weather metadata items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    road_weather_items: Union[Unset, 'RWItems'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rw_items import RWItems
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        road_weather_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.road_weather_items, Unset):
            road_weather_items = self.road_weather_items.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if road_weather_items is not UNSET:
            field_dict["road-weather-items"] = road_weather_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rw_items import RWItems
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        _road_weather_items = d.pop("road-weather-items", UNSET)
        road_weather_items: Union[Unset, RWItems]
        if isinstance(_road_weather_items,  Unset):
            road_weather_items = UNSET
        else:
            road_weather_items = RWItems.from_dict(_road_weather_items)




        rw_metadata = cls(
            organization_information=organization_information,
            road_weather_items=road_weather_items,
        )


        rw_metadata.additional_properties = d
        return rw_metadata

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
