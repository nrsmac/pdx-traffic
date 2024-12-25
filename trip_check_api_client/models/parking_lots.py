from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.mfp_calculation import MfpCalculation
  from ..models.mfp_lot_data import MfpLotData





T = TypeVar("T", bound="ParkingLots")


@_attrs_define
class ParkingLots:
    """ Parking Lot Information and Data class

        Attributes:
            parking_lot_calculation (Union[Unset, MfpCalculation]): Parking lot location and percentage information
            parking_lot_data_array (Union[Unset, list['MfpLotData']]): Array of collections of parking lot data
     """

    parking_lot_calculation: Union[Unset, 'MfpCalculation'] = UNSET
    parking_lot_data_array: Union[Unset, list['MfpLotData']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.mfp_calculation import MfpCalculation
        from ..models.mfp_lot_data import MfpLotData
        parking_lot_calculation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parking_lot_calculation, Unset):
            parking_lot_calculation = self.parking_lot_calculation.to_dict()

        parking_lot_data_array: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parking_lot_data_array, Unset):
            parking_lot_data_array = []
            for parking_lot_data_array_item_data in self.parking_lot_data_array:
                parking_lot_data_array_item = parking_lot_data_array_item_data.to_dict()
                parking_lot_data_array.append(parking_lot_data_array_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if parking_lot_calculation is not UNSET:
            field_dict["parkingLotCalculation"] = parking_lot_calculation
        if parking_lot_data_array is not UNSET:
            field_dict["parkingLotDataArray"] = parking_lot_data_array

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.mfp_calculation import MfpCalculation
        from ..models.mfp_lot_data import MfpLotData
        d = src_dict.copy()
        _parking_lot_calculation = d.pop("parkingLotCalculation", UNSET)
        parking_lot_calculation: Union[Unset, MfpCalculation]
        if isinstance(_parking_lot_calculation,  Unset):
            parking_lot_calculation = UNSET
        else:
            parking_lot_calculation = MfpCalculation.from_dict(_parking_lot_calculation)




        parking_lot_data_array = []
        _parking_lot_data_array = d.pop("parkingLotDataArray", UNSET)
        for parking_lot_data_array_item_data in (_parking_lot_data_array or []):
            parking_lot_data_array_item = MfpLotData.from_dict(parking_lot_data_array_item_data)



            parking_lot_data_array.append(parking_lot_data_array_item)


        parking_lots = cls(
            parking_lot_calculation=parking_lot_calculation,
            parking_lot_data_array=parking_lot_data_array,
        )


        parking_lots.additional_properties = d
        return parking_lots

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
