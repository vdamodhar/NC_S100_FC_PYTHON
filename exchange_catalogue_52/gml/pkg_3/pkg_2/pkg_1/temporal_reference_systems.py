from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlTime
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.deprecated_types import StringOrRefType
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.dictionary import DefinitionType
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.gml_base import ReferenceType
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.temporal import (
    RelatedTimeType,
    TimeInstantPropertyType,
    TimeIntervalLengthType,
    TimePeriodPropertyType,
    TimePositionType,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.temporal_topology import TimeNodePropertyType
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarEraType(DefinitionType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    reference_date: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    julian_reference: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    epoch_of_use: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TimeOrdinalEraType(DefinitionType):
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    start: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    end: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    extent: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    member: List["TimeOrdinalEraPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    group: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeReferenceSystemType(DefinitionType):
    domain_of_validity: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TimeCalendarEra(TimeCalendarEraType):
    """Gml:TimeCalendarEra inherits basic properties from gml:DefinitionType and
    has the following additional properties:

    -       gml:referenceEvent is the name or description of a mythical or historic event which fixes the position of the base scale of the calendar era.  This is given as text or using a link to description held elsewhere.
    -       gml:referenceDate specifies the date of the referenceEvent expressed as a date in the given calendar.  In most calendars, this date is the origin (i.e., the first day) of the scale, but this is not always true.
    -       gml:julianReference specifies the Julian date that corresponds to the reference date.  The Julian day number is an integer value; the Julian date is a decimal value that allows greater resolution.  Transforming calendar dates to and from Julian dates provides a relatively simple basis for transforming dates from one calendar to another.
    -       gml:epochOfUse is the period for which the calendar era was used as a basis for dating.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCoordinateSystemType(TimeReferenceSystemType):
    origin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    origin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TimeOrdinalEra(TimeOrdinalEraType):
    """Its content model follows the pattern of gml:TimeEdge, inheriting standard
    properties from gml:DefinitionType, and adding gml:start, gml:end and
    gml:extent properties, a set of gml:member properties which indicate ordered
    gml:TimeOrdinalEra elements, and a gml:group property which points to the
    parent era.

    The recursive inclusion of gml:TimeOrdinalEra elements allow the
    construction of an arbitrary depth hierarchical ordinal reference
    schema, such that an ordinal era at a given level of the hierarchy
    includes a sequence of shorter, coterminous ordinal eras.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeReferenceSystem(TimeReferenceSystemType):
    """A reference system is characterized in terms of its domain of validity: the spatial and temporal extent over which it is applicable. The basic GML element for temporal reference systems is gml:TimeReferenceSystem.  Its content model extends gml:DefinitionType with one additional property, gml:domainOfValidity."""
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarEraPropertyType:
    """
    Gml:TimeCalendarEraPropertyType provides for associating a gml:TimeCalendarEra
    with an object.
    """
    time_calendar_era: Optional[TimeCalendarEra] = field(
        default=None,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeCoordinateSystem(TimeCoordinateSystemType):
    """A temporal coordinate system shall be based on a continuous interval scale
    defined in terms of a single time interval.

    The differences to ISO 19108 TM_CoordinateSystem are:
    -       the origin is specified either using the property gml:originPosition whose value is a direct time position, or using the property gml:origin whose model is gml:TimeInstantPropertyType; this permits more flexibility in representation and also supports referring to a value fixed elsewhere;
    -       the interval uses gml:TimeIntervalLengthType.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeOrdinalEraPropertyType:
    """
    Gml:TimeOrdinalEraPropertyType provides for associating a gml:TimeOrdinalEra
    with an object.
    """
    time_ordinal_era: Optional[TimeOrdinalEra] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeCalendarType(TimeReferenceSystemType):
    reference_frame: List[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeOrdinalReferenceSystemType(TimeReferenceSystemType):
    component: List[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeCalendar(TimeCalendarType):
    """A calendar is a discrete temporal reference system that provides a basis for
    defining temporal position to a resolution of one day.

    gml:TimeCalendar adds one property to those inherited from
    gml:TimeReferenceSystem. A gml:referenceFrame provides a link to a
    gml:TimeCalendarEra that it uses. A  gml:TimeCalendar may reference
    more than one calendar era. The referenceFrame element follows the
    standard GML property model, allowing the association to be
    instantiated either using an inline description using the
    gml:TimeCalendarEra element, or a link to a gml:TimeCalendarEra
    which is explicit elsewhere.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeOrdinalReferenceSystem(TimeOrdinalReferenceSystemType):
    """In some applications of geographic information — such as geology and
    archaeology — relative position in time is known more precisely than absolute
    time or duration.

    The order of events in time can be well established, but the
    magnitude of the intervals between them cannot be accurately
    determined; in such cases, the use of an ordinal temporal reference
    system is appropriate. An ordinal temporal reference system is
    composed of a sequence of named coterminous eras, which may in turn
    be composed of sequences of member eras at a finer scale, giving the
    whole a hierarchical structure of eras of verying resolution. An
    ordinal temporal reference system whose component eras are not
    further subdivided is effectively a temporal topological complex
    constrained to be a linear graph. An ordinal temporal reference
    system some or all of whose component eras are subdivided is
    effectively a temporal topological complex with the constraint that
    parallel branches may only be constructed in pairs where one is a
    single temporal ordinal era and the other is a sequence of temporal
    ordinal eras that are called "members" of the "group". This
    constraint means that within a single temporal ordinal reference
    system, the relative position of all temporal ordinal eras is
    unambiguous. The positions of the beginning and end of a given era
    may calibrate the relative time scale.
    gml:TimeOrdinalReferenceSystem adds one or more gml:component
    properties to the generic temporal reference system model.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarPropertyType:
    """
    Gml:TimeCalendarPropertyType provides for associating a gml:TimeCalendar with
    an object.
    """
    time_calendar: Optional[TimeCalendar] = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeClockType(TimeReferenceSystemType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "referenceTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    utc_reference: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "utcReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    date_basis: List[TimeCalendarPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateBasis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeClock(TimeClockType):
    """A clock provides a basis for defining temporal position within a day. A
    clock shall be used with a calendar in order to provide a complete description
    of a temporal position within a specific day.

    gml:TimeClock adds the following properties to those inherited from gml:TimeReferenceSystemType:
    -       gml:referenceEvent is the name or description of an event, such as solar noon or sunrise, which fixes the position of the base scale of the clock.
    -       gml:referenceTime specifies the time of day associated with the reference event expressed as a time of day in the given clock. The reference time is usually the origin of the clock scale.
    -       gml:utcReference specifies the 24 hour local or UTC time that corresponds to the reference time.
    -       gml:dateBasis contains or references the calendars that use this clock.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeClockPropertyType:
    """
    Gml:TimeClockPropertyType provides for associating a gml:TimeClock with an
    object.
    """
    time_clock: Optional[TimeClock] = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
