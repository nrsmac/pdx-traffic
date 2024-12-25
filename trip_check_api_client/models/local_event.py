from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="LocalEvent")


@_attrs_define
class LocalEvent:
    """ TLE Event Item

        Attributes:
            id (Union[Unset, int]): Event Id
            location_description (Union[Unset, str]): Description of the event location
            type_ (Union[Unset, str]): Event type
            impact (Union[Unset, str]): Event impact
            headline (Union[Unset, str]): Event headline text
            comments (Union[Unset, str]): Event comments
            create_time (Union[Unset, datetime.datetime]): Event creation timestamp
            event_start (Union[Unset, datetime.datetime]): Event publish date
            event_end (Union[Unset, datetime.datetime]): Event remove date
            start_lat (Union[Unset, float]): Head latitude for point and line events
            start_long (Union[Unset, float]): Head longitude for point and line events
            end_lat (Union[Unset, float]): Tail latitude for line events
            end_long (Union[Unset, float]): Tail longitude for line events
            geometry_wkt (Union[Unset, str]): Geometry well-known text for line and area events
            source_agency (Union[Unset, str]): Source agency
            contact_email (Union[Unset, str]): Contact email
            contact_name (Union[Unset, str]): Contact name
            contact_organization (Union[Unset, str]): Contact organization
            contact_phone (Union[Unset, str]): Contact phone number
            direction (Union[Unset, str]): Direction impacted [ ONE_DIRECTION | BOTH_DIRECTIONS ]
            update_time (Union[Unset, datetime.datetime]): Last updated timestamp
     """

    id: Union[Unset, int] = UNSET
    location_description: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    create_time: Union[Unset, datetime.datetime] = UNSET
    event_start: Union[Unset, datetime.datetime] = UNSET
    event_end: Union[Unset, datetime.datetime] = UNSET
    start_lat: Union[Unset, float] = UNSET
    start_long: Union[Unset, float] = UNSET
    end_lat: Union[Unset, float] = UNSET
    end_long: Union[Unset, float] = UNSET
    geometry_wkt: Union[Unset, str] = UNSET
    source_agency: Union[Unset, str] = UNSET
    contact_email: Union[Unset, str] = UNSET
    contact_name: Union[Unset, str] = UNSET
    contact_organization: Union[Unset, str] = UNSET
    contact_phone: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    update_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        location_description = self.location_description

        type_ = self.type_

        impact = self.impact

        headline = self.headline

        comments = self.comments

        create_time: Union[Unset, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        event_start: Union[Unset, str] = UNSET
        if not isinstance(self.event_start, Unset):
            event_start = self.event_start.isoformat()

        event_end: Union[Unset, str] = UNSET
        if not isinstance(self.event_end, Unset):
            event_end = self.event_end.isoformat()

        start_lat = self.start_lat

        start_long = self.start_long

        end_lat = self.end_lat

        end_long = self.end_long

        geometry_wkt = self.geometry_wkt

        source_agency = self.source_agency

        contact_email = self.contact_email

        contact_name = self.contact_name

        contact_organization = self.contact_organization

        contact_phone = self.contact_phone

        direction = self.direction

        update_time: Union[Unset, str] = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["Id"] = id
        if location_description is not UNSET:
            field_dict["LocationDescription"] = location_description
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if impact is not UNSET:
            field_dict["Impact"] = impact
        if headline is not UNSET:
            field_dict["Headline"] = headline
        if comments is not UNSET:
            field_dict["Comments"] = comments
        if create_time is not UNSET:
            field_dict["CreateTime"] = create_time
        if event_start is not UNSET:
            field_dict["EventStart"] = event_start
        if event_end is not UNSET:
            field_dict["EventEnd"] = event_end
        if start_lat is not UNSET:
            field_dict["StartLat"] = start_lat
        if start_long is not UNSET:
            field_dict["StartLong"] = start_long
        if end_lat is not UNSET:
            field_dict["EndLat"] = end_lat
        if end_long is not UNSET:
            field_dict["EndLong"] = end_long
        if geometry_wkt is not UNSET:
            field_dict["GeometryWkt"] = geometry_wkt
        if source_agency is not UNSET:
            field_dict["SourceAgency"] = source_agency
        if contact_email is not UNSET:
            field_dict["ContactEmail"] = contact_email
        if contact_name is not UNSET:
            field_dict["ContactName"] = contact_name
        if contact_organization is not UNSET:
            field_dict["ContactOrganization"] = contact_organization
        if contact_phone is not UNSET:
            field_dict["ContactPhone"] = contact_phone
        if direction is not UNSET:
            field_dict["Direction"] = direction
        if update_time is not UNSET:
            field_dict["UpdateTime"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        location_description = d.pop("LocationDescription", UNSET)

        type_ = d.pop("Type", UNSET)

        impact = d.pop("Impact", UNSET)

        headline = d.pop("Headline", UNSET)

        comments = d.pop("Comments", UNSET)

        _create_time = d.pop("CreateTime", UNSET)
        create_time: Union[Unset, datetime.datetime]
        if isinstance(_create_time,  Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)




        _event_start = d.pop("EventStart", UNSET)
        event_start: Union[Unset, datetime.datetime]
        if isinstance(_event_start,  Unset):
            event_start = UNSET
        else:
            event_start = isoparse(_event_start)




        _event_end = d.pop("EventEnd", UNSET)
        event_end: Union[Unset, datetime.datetime]
        if isinstance(_event_end,  Unset):
            event_end = UNSET
        else:
            event_end = isoparse(_event_end)




        start_lat = d.pop("StartLat", UNSET)

        start_long = d.pop("StartLong", UNSET)

        end_lat = d.pop("EndLat", UNSET)

        end_long = d.pop("EndLong", UNSET)

        geometry_wkt = d.pop("GeometryWkt", UNSET)

        source_agency = d.pop("SourceAgency", UNSET)

        contact_email = d.pop("ContactEmail", UNSET)

        contact_name = d.pop("ContactName", UNSET)

        contact_organization = d.pop("ContactOrganization", UNSET)

        contact_phone = d.pop("ContactPhone", UNSET)

        direction = d.pop("Direction", UNSET)

        _update_time = d.pop("UpdateTime", UNSET)
        update_time: Union[Unset, datetime.datetime]
        if isinstance(_update_time,  Unset):
            update_time = UNSET
        else:
            update_time = isoparse(_update_time)




        local_event = cls(
            id=id,
            location_description=location_description,
            type_=type_,
            impact=impact,
            headline=headline,
            comments=comments,
            create_time=create_time,
            event_start=event_start,
            event_end=event_end,
            start_lat=start_lat,
            start_long=start_long,
            end_lat=end_lat,
            end_long=end_long,
            geometry_wkt=geometry_wkt,
            source_agency=source_agency,
            contact_email=contact_email,
            contact_name=contact_name,
            contact_organization=contact_organization,
            contact_phone=contact_phone,
            direction=direction,
            update_time=update_time,
        )


        local_event.additional_properties = d
        return local_event

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
