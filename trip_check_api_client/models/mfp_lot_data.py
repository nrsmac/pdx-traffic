from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="MfpLotData")


@_attrs_define
class MfpLotData:
    """ Collection of parking lot information and data

        Attributes:
            lot_sum_id (Union[Unset, int]): Identifier for this lot sum object
            lot_cap_pct_no (Union[Unset, int]): Lot capacity percent
            gate_stat_close_thrshld_no (Union[Unset, int]): Gate status close threshold
            gate_stat_open_thrshld_no (Union[Unset, int]): Gate status open threshold
            car_cnt_day_no (Union[Unset, int]): Car count for the day
            cur_car_cnt_no (Union[Unset, int]): Current car count
            gate_sys_stat_no (Union[Unset, int]): Gate system status
            blk_out_sign_pos_no (Union[Unset, int]): Blank out sign position
            gate_1_alm_no (Union[Unset, int]): Gate 1 alarm number
            gate_2_alm_no (Union[Unset, int]): Gate 2 alarm number
            gate_3_alm_no (Union[Unset, int]): Gate 3 alarm number
            gate_4_alm_no (Union[Unset, int]): Gate 4 alarm number
            bos_1_stat_alm_no (Union[Unset, int]): Bos. 1 status alarm number
            bos_2_stat_alm_no (Union[Unset, int]): Bos. 2 status alarm number
            bos_3_stat_alm_no (Union[Unset, int]): Bos. 3 status alarm number
            bos_4_stat_alm_no (Union[Unset, int]): Bos. 4 status alarm number
            gate_1_stat_pos_no (Union[Unset, int]): Gate 1 status position number
            gate_2_stat_pos_no (Union[Unset, int]): Gate 2 status position number
            gate_3_stat_pos_no (Union[Unset, int]): Gate 3 status position number
            gate_4_stat_pos_no (Union[Unset, int]): Gate 4 status position number
            gate_1_dtctr_fail_alm_no (Union[Unset, int]): Gate 1 detector fail alarm number
            gate_2_dtctr_fail_alm_no (Union[Unset, int]): Gate 2 detector fail alarm number
            gate_3_dtctr_fail_alm_no (Union[Unset, int]): Gate 3 detector fail alarm number
            gate_4_dtctr_fail_alm_no (Union[Unset, int]): Gate 4 detector fail alarm number
            gate_1_dtctr_fail_cd_no (Union[Unset, int]): Gate 1 detector fail code
            gate_2_dtctr_fail_cd_no (Union[Unset, int]): Gate 2 detector fail code
            gate_3_dtctr_fail_cd_no (Union[Unset, int]): Gate 3 detector fail code
            gate_4_dtctr_fail_cd_no (Union[Unset, int]): Gate 4 detector fail code
            man_stat_cd (Union[Unset, int]): Man. status code
            ud_dttm (Union[Unset, datetime.datetime]): Last update time
     """

    lot_sum_id: Union[Unset, int] = UNSET
    lot_cap_pct_no: Union[Unset, int] = UNSET
    gate_stat_close_thrshld_no: Union[Unset, int] = UNSET
    gate_stat_open_thrshld_no: Union[Unset, int] = UNSET
    car_cnt_day_no: Union[Unset, int] = UNSET
    cur_car_cnt_no: Union[Unset, int] = UNSET
    gate_sys_stat_no: Union[Unset, int] = UNSET
    blk_out_sign_pos_no: Union[Unset, int] = UNSET
    gate_1_alm_no: Union[Unset, int] = UNSET
    gate_2_alm_no: Union[Unset, int] = UNSET
    gate_3_alm_no: Union[Unset, int] = UNSET
    gate_4_alm_no: Union[Unset, int] = UNSET
    bos_1_stat_alm_no: Union[Unset, int] = UNSET
    bos_2_stat_alm_no: Union[Unset, int] = UNSET
    bos_3_stat_alm_no: Union[Unset, int] = UNSET
    bos_4_stat_alm_no: Union[Unset, int] = UNSET
    gate_1_stat_pos_no: Union[Unset, int] = UNSET
    gate_2_stat_pos_no: Union[Unset, int] = UNSET
    gate_3_stat_pos_no: Union[Unset, int] = UNSET
    gate_4_stat_pos_no: Union[Unset, int] = UNSET
    gate_1_dtctr_fail_alm_no: Union[Unset, int] = UNSET
    gate_2_dtctr_fail_alm_no: Union[Unset, int] = UNSET
    gate_3_dtctr_fail_alm_no: Union[Unset, int] = UNSET
    gate_4_dtctr_fail_alm_no: Union[Unset, int] = UNSET
    gate_1_dtctr_fail_cd_no: Union[Unset, int] = UNSET
    gate_2_dtctr_fail_cd_no: Union[Unset, int] = UNSET
    gate_3_dtctr_fail_cd_no: Union[Unset, int] = UNSET
    gate_4_dtctr_fail_cd_no: Union[Unset, int] = UNSET
    man_stat_cd: Union[Unset, int] = UNSET
    ud_dttm: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        lot_sum_id = self.lot_sum_id

        lot_cap_pct_no = self.lot_cap_pct_no

        gate_stat_close_thrshld_no = self.gate_stat_close_thrshld_no

        gate_stat_open_thrshld_no = self.gate_stat_open_thrshld_no

        car_cnt_day_no = self.car_cnt_day_no

        cur_car_cnt_no = self.cur_car_cnt_no

        gate_sys_stat_no = self.gate_sys_stat_no

        blk_out_sign_pos_no = self.blk_out_sign_pos_no

        gate_1_alm_no = self.gate_1_alm_no

        gate_2_alm_no = self.gate_2_alm_no

        gate_3_alm_no = self.gate_3_alm_no

        gate_4_alm_no = self.gate_4_alm_no

        bos_1_stat_alm_no = self.bos_1_stat_alm_no

        bos_2_stat_alm_no = self.bos_2_stat_alm_no

        bos_3_stat_alm_no = self.bos_3_stat_alm_no

        bos_4_stat_alm_no = self.bos_4_stat_alm_no

        gate_1_stat_pos_no = self.gate_1_stat_pos_no

        gate_2_stat_pos_no = self.gate_2_stat_pos_no

        gate_3_stat_pos_no = self.gate_3_stat_pos_no

        gate_4_stat_pos_no = self.gate_4_stat_pos_no

        gate_1_dtctr_fail_alm_no = self.gate_1_dtctr_fail_alm_no

        gate_2_dtctr_fail_alm_no = self.gate_2_dtctr_fail_alm_no

        gate_3_dtctr_fail_alm_no = self.gate_3_dtctr_fail_alm_no

        gate_4_dtctr_fail_alm_no = self.gate_4_dtctr_fail_alm_no

        gate_1_dtctr_fail_cd_no = self.gate_1_dtctr_fail_cd_no

        gate_2_dtctr_fail_cd_no = self.gate_2_dtctr_fail_cd_no

        gate_3_dtctr_fail_cd_no = self.gate_3_dtctr_fail_cd_no

        gate_4_dtctr_fail_cd_no = self.gate_4_dtctr_fail_cd_no

        man_stat_cd = self.man_stat_cd

        ud_dttm: Union[Unset, str] = UNSET
        if not isinstance(self.ud_dttm, Unset):
            ud_dttm = self.ud_dttm.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if lot_sum_id is not UNSET:
            field_dict["LOT_SUM_ID"] = lot_sum_id
        if lot_cap_pct_no is not UNSET:
            field_dict["LOT_CAP_PCT_NO"] = lot_cap_pct_no
        if gate_stat_close_thrshld_no is not UNSET:
            field_dict["GATE_STAT_CLOSE_THRSHLD_NO"] = gate_stat_close_thrshld_no
        if gate_stat_open_thrshld_no is not UNSET:
            field_dict["GATE_STAT_OPEN_THRSHLD_NO"] = gate_stat_open_thrshld_no
        if car_cnt_day_no is not UNSET:
            field_dict["CAR_CNT_DAY_NO"] = car_cnt_day_no
        if cur_car_cnt_no is not UNSET:
            field_dict["CUR_CAR_CNT_NO"] = cur_car_cnt_no
        if gate_sys_stat_no is not UNSET:
            field_dict["GATE_SYS_STAT_NO"] = gate_sys_stat_no
        if blk_out_sign_pos_no is not UNSET:
            field_dict["BLK_OUT_SIGN_POS_NO"] = blk_out_sign_pos_no
        if gate_1_alm_no is not UNSET:
            field_dict["GATE_1_ALM_NO"] = gate_1_alm_no
        if gate_2_alm_no is not UNSET:
            field_dict["GATE_2_ALM_NO"] = gate_2_alm_no
        if gate_3_alm_no is not UNSET:
            field_dict["GATE_3_ALM_NO"] = gate_3_alm_no
        if gate_4_alm_no is not UNSET:
            field_dict["GATE_4_ALM_NO"] = gate_4_alm_no
        if bos_1_stat_alm_no is not UNSET:
            field_dict["BOS_1_STAT_ALM_NO"] = bos_1_stat_alm_no
        if bos_2_stat_alm_no is not UNSET:
            field_dict["BOS_2_STAT_ALM_NO"] = bos_2_stat_alm_no
        if bos_3_stat_alm_no is not UNSET:
            field_dict["BOS_3_STAT_ALM_NO"] = bos_3_stat_alm_no
        if bos_4_stat_alm_no is not UNSET:
            field_dict["BOS_4_STAT_ALM_NO"] = bos_4_stat_alm_no
        if gate_1_stat_pos_no is not UNSET:
            field_dict["GATE_1_STAT_POS_NO"] = gate_1_stat_pos_no
        if gate_2_stat_pos_no is not UNSET:
            field_dict["GATE_2_STAT_POS_NO"] = gate_2_stat_pos_no
        if gate_3_stat_pos_no is not UNSET:
            field_dict["GATE_3_STAT_POS_NO"] = gate_3_stat_pos_no
        if gate_4_stat_pos_no is not UNSET:
            field_dict["GATE_4_STAT_POS_NO"] = gate_4_stat_pos_no
        if gate_1_dtctr_fail_alm_no is not UNSET:
            field_dict["GATE_1_DTCTR_FAIL_ALM_NO"] = gate_1_dtctr_fail_alm_no
        if gate_2_dtctr_fail_alm_no is not UNSET:
            field_dict["GATE_2_DTCTR_FAIL_ALM_NO"] = gate_2_dtctr_fail_alm_no
        if gate_3_dtctr_fail_alm_no is not UNSET:
            field_dict["GATE_3_DTCTR_FAIL_ALM_NO"] = gate_3_dtctr_fail_alm_no
        if gate_4_dtctr_fail_alm_no is not UNSET:
            field_dict["GATE_4_DTCTR_FAIL_ALM_NO"] = gate_4_dtctr_fail_alm_no
        if gate_1_dtctr_fail_cd_no is not UNSET:
            field_dict["GATE_1_DTCTR_FAIL_CD_NO"] = gate_1_dtctr_fail_cd_no
        if gate_2_dtctr_fail_cd_no is not UNSET:
            field_dict["GATE_2_DTCTR_FAIL_CD_NO"] = gate_2_dtctr_fail_cd_no
        if gate_3_dtctr_fail_cd_no is not UNSET:
            field_dict["GATE_3_DTCTR_FAIL_CD_NO"] = gate_3_dtctr_fail_cd_no
        if gate_4_dtctr_fail_cd_no is not UNSET:
            field_dict["GATE_4_DTCTR_FAIL_CD_NO"] = gate_4_dtctr_fail_cd_no
        if man_stat_cd is not UNSET:
            field_dict["MAN_STAT_CD"] = man_stat_cd
        if ud_dttm is not UNSET:
            field_dict["UD_DTTM"] = ud_dttm

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lot_sum_id = d.pop("LOT_SUM_ID", UNSET)

        lot_cap_pct_no = d.pop("LOT_CAP_PCT_NO", UNSET)

        gate_stat_close_thrshld_no = d.pop("GATE_STAT_CLOSE_THRSHLD_NO", UNSET)

        gate_stat_open_thrshld_no = d.pop("GATE_STAT_OPEN_THRSHLD_NO", UNSET)

        car_cnt_day_no = d.pop("CAR_CNT_DAY_NO", UNSET)

        cur_car_cnt_no = d.pop("CUR_CAR_CNT_NO", UNSET)

        gate_sys_stat_no = d.pop("GATE_SYS_STAT_NO", UNSET)

        blk_out_sign_pos_no = d.pop("BLK_OUT_SIGN_POS_NO", UNSET)

        gate_1_alm_no = d.pop("GATE_1_ALM_NO", UNSET)

        gate_2_alm_no = d.pop("GATE_2_ALM_NO", UNSET)

        gate_3_alm_no = d.pop("GATE_3_ALM_NO", UNSET)

        gate_4_alm_no = d.pop("GATE_4_ALM_NO", UNSET)

        bos_1_stat_alm_no = d.pop("BOS_1_STAT_ALM_NO", UNSET)

        bos_2_stat_alm_no = d.pop("BOS_2_STAT_ALM_NO", UNSET)

        bos_3_stat_alm_no = d.pop("BOS_3_STAT_ALM_NO", UNSET)

        bos_4_stat_alm_no = d.pop("BOS_4_STAT_ALM_NO", UNSET)

        gate_1_stat_pos_no = d.pop("GATE_1_STAT_POS_NO", UNSET)

        gate_2_stat_pos_no = d.pop("GATE_2_STAT_POS_NO", UNSET)

        gate_3_stat_pos_no = d.pop("GATE_3_STAT_POS_NO", UNSET)

        gate_4_stat_pos_no = d.pop("GATE_4_STAT_POS_NO", UNSET)

        gate_1_dtctr_fail_alm_no = d.pop("GATE_1_DTCTR_FAIL_ALM_NO", UNSET)

        gate_2_dtctr_fail_alm_no = d.pop("GATE_2_DTCTR_FAIL_ALM_NO", UNSET)

        gate_3_dtctr_fail_alm_no = d.pop("GATE_3_DTCTR_FAIL_ALM_NO", UNSET)

        gate_4_dtctr_fail_alm_no = d.pop("GATE_4_DTCTR_FAIL_ALM_NO", UNSET)

        gate_1_dtctr_fail_cd_no = d.pop("GATE_1_DTCTR_FAIL_CD_NO", UNSET)

        gate_2_dtctr_fail_cd_no = d.pop("GATE_2_DTCTR_FAIL_CD_NO", UNSET)

        gate_3_dtctr_fail_cd_no = d.pop("GATE_3_DTCTR_FAIL_CD_NO", UNSET)

        gate_4_dtctr_fail_cd_no = d.pop("GATE_4_DTCTR_FAIL_CD_NO", UNSET)

        man_stat_cd = d.pop("MAN_STAT_CD", UNSET)

        _ud_dttm = d.pop("UD_DTTM", UNSET)
        ud_dttm: Union[Unset, datetime.datetime]
        if isinstance(_ud_dttm,  Unset):
            ud_dttm = UNSET
        else:
            ud_dttm = isoparse(_ud_dttm)




        mfp_lot_data = cls(
            lot_sum_id=lot_sum_id,
            lot_cap_pct_no=lot_cap_pct_no,
            gate_stat_close_thrshld_no=gate_stat_close_thrshld_no,
            gate_stat_open_thrshld_no=gate_stat_open_thrshld_no,
            car_cnt_day_no=car_cnt_day_no,
            cur_car_cnt_no=cur_car_cnt_no,
            gate_sys_stat_no=gate_sys_stat_no,
            blk_out_sign_pos_no=blk_out_sign_pos_no,
            gate_1_alm_no=gate_1_alm_no,
            gate_2_alm_no=gate_2_alm_no,
            gate_3_alm_no=gate_3_alm_no,
            gate_4_alm_no=gate_4_alm_no,
            bos_1_stat_alm_no=bos_1_stat_alm_no,
            bos_2_stat_alm_no=bos_2_stat_alm_no,
            bos_3_stat_alm_no=bos_3_stat_alm_no,
            bos_4_stat_alm_no=bos_4_stat_alm_no,
            gate_1_stat_pos_no=gate_1_stat_pos_no,
            gate_2_stat_pos_no=gate_2_stat_pos_no,
            gate_3_stat_pos_no=gate_3_stat_pos_no,
            gate_4_stat_pos_no=gate_4_stat_pos_no,
            gate_1_dtctr_fail_alm_no=gate_1_dtctr_fail_alm_no,
            gate_2_dtctr_fail_alm_no=gate_2_dtctr_fail_alm_no,
            gate_3_dtctr_fail_alm_no=gate_3_dtctr_fail_alm_no,
            gate_4_dtctr_fail_alm_no=gate_4_dtctr_fail_alm_no,
            gate_1_dtctr_fail_cd_no=gate_1_dtctr_fail_cd_no,
            gate_2_dtctr_fail_cd_no=gate_2_dtctr_fail_cd_no,
            gate_3_dtctr_fail_cd_no=gate_3_dtctr_fail_cd_no,
            gate_4_dtctr_fail_cd_no=gate_4_dtctr_fail_cd_no,
            man_stat_cd=man_stat_cd,
            ud_dttm=ud_dttm,
        )


        mfp_lot_data.additional_properties = d
        return mfp_lot_data

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
