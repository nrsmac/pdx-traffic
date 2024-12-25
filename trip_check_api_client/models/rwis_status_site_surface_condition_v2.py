from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_status_site_sensor_v2 import RwisStatusSiteSensorV2





T = TypeVar("T", bound="RwisStatusSiteSurfaceConditionV2")


@_attrs_define
class RwisStatusSiteSurfaceConditionV2:
    """ Surface Conditions

        Attributes:
            mobile_friction (Union[Unset, int]): Mobile friction: essMobileFriction, percent (0..100), error: 101
            surface_freeze_point (Union[Unset, int]): Surface freeze point: essSurfaceFreezePoint, tenth degree C
                (-1000..1000), error: 1001
            surface_salinity (Union[Unset, int]): Surface salinity: essSurfaceSalinity, parts per 100,000, error: 65535
            surface_temperatures (Union[Unset, list['RwisStatusSiteSensorV2']]): Sub-Surface Conditions
            water_depth (Union[Unset, int]): Water depth: essSurfaceIceOrWaterDepth, tenth millimeters (0..65535), error:
                65535
     """

    mobile_friction: Union[Unset, int] = UNSET
    surface_freeze_point: Union[Unset, int] = UNSET
    surface_salinity: Union[Unset, int] = UNSET
    surface_temperatures: Union[Unset, list['RwisStatusSiteSensorV2']] = UNSET
    water_depth: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_status_site_sensor_v2 import RwisStatusSiteSensorV2
        mobile_friction = self.mobile_friction

        surface_freeze_point = self.surface_freeze_point

        surface_salinity = self.surface_salinity

        surface_temperatures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.surface_temperatures, Unset):
            surface_temperatures = []
            for surface_temperatures_item_data in self.surface_temperatures:
                surface_temperatures_item = surface_temperatures_item_data.to_dict()
                surface_temperatures.append(surface_temperatures_item)



        water_depth = self.water_depth


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mobile_friction is not UNSET:
            field_dict["mobile-friction"] = mobile_friction
        if surface_freeze_point is not UNSET:
            field_dict["surface-freeze-point"] = surface_freeze_point
        if surface_salinity is not UNSET:
            field_dict["surface-salinity"] = surface_salinity
        if surface_temperatures is not UNSET:
            field_dict["surface-temperatures"] = surface_temperatures
        if water_depth is not UNSET:
            field_dict["water-depth"] = water_depth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_status_site_sensor_v2 import RwisStatusSiteSensorV2
        d = src_dict.copy()
        mobile_friction = d.pop("mobile-friction", UNSET)

        surface_freeze_point = d.pop("surface-freeze-point", UNSET)

        surface_salinity = d.pop("surface-salinity", UNSET)

        surface_temperatures = []
        _surface_temperatures = d.pop("surface-temperatures", UNSET)
        for surface_temperatures_item_data in (_surface_temperatures or []):
            surface_temperatures_item = RwisStatusSiteSensorV2.from_dict(surface_temperatures_item_data)



            surface_temperatures.append(surface_temperatures_item)


        water_depth = d.pop("water-depth", UNSET)

        rwis_status_site_surface_condition_v2 = cls(
            mobile_friction=mobile_friction,
            surface_freeze_point=surface_freeze_point,
            surface_salinity=surface_salinity,
            surface_temperatures=surface_temperatures,
            water_depth=water_depth,
        )


        rwis_status_site_surface_condition_v2.additional_properties = d
        return rwis_status_site_surface_condition_v2

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
