from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_status_site_sensor import RwisStatusSiteSensor





T = TypeVar("T", bound="RwisStatusSiteSurfaceCondition")


@_attrs_define
class RwisStatusSiteSurfaceCondition:
    """ RWIS Status Site Surface Conditions Info

        Attributes:
            ice_thickness (Union[Unset, int]): Ice thickness
            mobile_friction (Union[Unset, int]): Mobile friction
            surface_freeze_point (Union[Unset, int]): Surface freeze point
            surface_salinity (Union[Unset, int]): Surface salinity
            surface_temperatures (Union[Unset, list['RwisStatusSiteSensor']]): Sub-surface conditions list
            surface_water_depth (Union[Unset, int]): Water level
            water_depth (Union[Unset, int]): Water depth
     """

    ice_thickness: Union[Unset, int] = UNSET
    mobile_friction: Union[Unset, int] = UNSET
    surface_freeze_point: Union[Unset, int] = UNSET
    surface_salinity: Union[Unset, int] = UNSET
    surface_temperatures: Union[Unset, list['RwisStatusSiteSensor']] = UNSET
    surface_water_depth: Union[Unset, int] = UNSET
    water_depth: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_status_site_sensor import RwisStatusSiteSensor
        ice_thickness = self.ice_thickness

        mobile_friction = self.mobile_friction

        surface_freeze_point = self.surface_freeze_point

        surface_salinity = self.surface_salinity

        surface_temperatures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.surface_temperatures, Unset):
            surface_temperatures = []
            for surface_temperatures_item_data in self.surface_temperatures:
                surface_temperatures_item = surface_temperatures_item_data.to_dict()
                surface_temperatures.append(surface_temperatures_item)



        surface_water_depth = self.surface_water_depth

        water_depth = self.water_depth


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ice_thickness is not UNSET:
            field_dict["ice-thickness"] = ice_thickness
        if mobile_friction is not UNSET:
            field_dict["mobile-friction"] = mobile_friction
        if surface_freeze_point is not UNSET:
            field_dict["surface-freeze-point"] = surface_freeze_point
        if surface_salinity is not UNSET:
            field_dict["surface-salinity"] = surface_salinity
        if surface_temperatures is not UNSET:
            field_dict["surface-temperatures"] = surface_temperatures
        if surface_water_depth is not UNSET:
            field_dict["surface-water-depth"] = surface_water_depth
        if water_depth is not UNSET:
            field_dict["water-depth"] = water_depth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_status_site_sensor import RwisStatusSiteSensor
        d = src_dict.copy()
        ice_thickness = d.pop("ice-thickness", UNSET)

        mobile_friction = d.pop("mobile-friction", UNSET)

        surface_freeze_point = d.pop("surface-freeze-point", UNSET)

        surface_salinity = d.pop("surface-salinity", UNSET)

        surface_temperatures = []
        _surface_temperatures = d.pop("surface-temperatures", UNSET)
        for surface_temperatures_item_data in (_surface_temperatures or []):
            surface_temperatures_item = RwisStatusSiteSensor.from_dict(surface_temperatures_item_data)



            surface_temperatures.append(surface_temperatures_item)


        surface_water_depth = d.pop("surface-water-depth", UNSET)

        water_depth = d.pop("water-depth", UNSET)

        rwis_status_site_surface_condition = cls(
            ice_thickness=ice_thickness,
            mobile_friction=mobile_friction,
            surface_freeze_point=surface_freeze_point,
            surface_salinity=surface_salinity,
            surface_temperatures=surface_temperatures,
            surface_water_depth=surface_water_depth,
            water_depth=water_depth,
        )


        rwis_status_site_surface_condition.additional_properties = d
        return rwis_status_site_surface_condition

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
