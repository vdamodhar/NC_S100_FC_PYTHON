from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.gml_base import AbstractGmltype
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class RelatedTimeTypeRelativePosition(Enum):
    BEFORE = "Before"
    AFTER = "After"
    BEGINS = "Begins"
    ENDS = "Ends"
    DURING = "During"
    EQUALS = "Equals"
    CONTAINS = "Contains"
    OVERLAPS = "Overlaps"
    MEETS = "Meets"
    OVERLAPPED_BY = "OverlappedBy"
    MET_BY = "MetBy"
    BEGUN_BY = "BegunBy"
    ENDED_BY = "EndedBy"


class TimeIndeterminateValueType(Enum):
    """These values are interpreted as follows:
    -	"unknown" indicates that no specific value for temporal position is provided.
    -	"now" indicates that the specified value shall be replaced with the current temporal position whenever the value is accessed.
    -	"before" indicates that the actual temporal position is unknown, but it is known to be before the specified value.
    -	"after" indicates that the actual temporal position is unknown, but it is known to be after the specified value.
    A value for indeterminatePosition may
    -	be used either alone, or
    -	qualify a specific value for temporal position."""
    AFTER = "after"
    BEFORE = "before"
    NOW = "now"
    UNKNOWN = "unknown"


class TimeUnitTypeValue(Enum):
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"


@dataclass
class Duration:
    """
    Gml:duration conforms to the ISO 8601 syntax for temporal length as implemented
    by the XML Schema duration type.
    """
    class Meta:
        name = "duration"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    pass


@dataclass
class TimeInstantPropertyType:
    """
    Gml:TimeInstantPropertyType provides for associating a gml:TimeInstant with an
    object.
    """
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeIntervalLengthType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: Optional[Union[str, TimeUnitTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"other:\w{2,}",
        }
    )
    radix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    factor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePositionType:
    """The method for identifying a temporal position is specific to each temporal
    reference system.

    gml:TimePositionType supports the description of temporal position
    according to the subtypes described in ISO 19108. Values based on
    calendars and clocks use lexical formats that are based on ISO 8601,
    as described in XML Schema Part 2:2001. A decimal value may be used
    with coordinate systems such as GPS time or UNIX time. A URI may be
    used to provide a reference to some era in an ordinal reference
    system . In common with many of the components modelled as data
    types in the ISO 19100 series of International Standards, the
    corresponding GML component has simple content. However, the content
    model gml:TimePositionType is defined in several steps. Three XML
    attributes appear on gml:TimePositionType: A time value shall be
    associated with a temporal reference system through the frame
    attribute that provides a URI reference that identifies a
    description of the reference system. Following ISO 19108, the
    Gregorian calendar with UTC is the default reference system, but
    others may also be used. Components for describing temporal
    reference systems are described in 14.4, but it is not required that
    the reference system be described in this, as the reference may
    refer to anything that may be indentified with a URI. For time
    values using a calendar containing more than one era, the (optional)
    calendarEraName attribute provides the name of the calendar era.
    Inexact temporal positions may be expressed using the optional
    indeterminatePosition attribute.  This takes a value from an
    enumeration.
    """
    value: Union[XmlDate, XmlPeriod, XmlTime, XmlDateTime, str, Decimal] = field(
        default=""
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )
    calendar_era_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "calendarEraName",
            "type": "Attribute",
        }
    )
    indeterminate_position: Optional[TimeIndeterminateValueType] = field(
        default=None,
        metadata={
            "name": "indeterminatePosition",
            "type": "Attribute",
        }
    )


@dataclass
class TimePrimitivePropertyType:
    """
    Gml:TimePrimitivePropertyType provides a standard content model for
    associations between an arbitrary member of the substitution group whose head
    is gml:AbstractTimePrimitive and another object.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_node: Optional["TimeNode"] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_period: Optional["TimePeriod"] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    pass


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    """Gml:RelatedTimeType provides a content model for indicating the relative
    position of an arbitrary member of the substitution group whose head is
    gml:AbstractTimePrimitive.

    It extends the generic gml:TimePrimitivePropertyType with an XML
    attribute relativePosition, whose value is selected from the set of
    13 temporal relationships identified by Allen (1983)
    """
    relative_position: Optional[RelatedTimeTypeRelativePosition] = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        }
    )


@dataclass
class TimeInterval(TimeIntervalLengthType):
    """Gml:timeInterval conforms to ISO 11404 which is based on floating point
    values for temporal length.

    ISO 11404 syntax specifies the use of a positiveInteger together
    with appropriate values for radix and factor. The resolution of the
    time interval is to one radix ^(-factor) of the specified time unit.
    The value of the unit is either selected from the units for time
    intervals from ISO 31-1:1992, or is another suitable unit.  The
    encoding is defined for GML in gml:TimeUnitType. The second
    component of this union type provides a method for indicating time
    units other than the six standard units given in the enumeration.
    """
    class Meta:
        name = "timeInterval"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimePosition(TimePositionType):
    """
    This element is used directly as a property of gml:TimeInstant (see 15.2.2.3),
    and may also be used in application schemas.
    """
    class Meta:
        name = "timePosition"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    """
    Gml:validTime is a convenience property element.
    """
    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class AbstractTimeGeometricPrimitiveType(AbstractTimePrimitiveType):
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeInstantType(AbstractTimeGeometricPrimitiveType):
    time_position: Optional[TimePosition] = field(
        default=None,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TimePeriodType(AbstractTimeGeometricPrimitiveType):
    begin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    begin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    end_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    end: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_interval: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TimeInstant(TimeInstantType):
    """
    Gml:TimeInstant acts as a zero-dimensional geometric primitive that represents
    an identifiable position in time.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimePeriod(TimePeriodType):
    """Gml:TimePeriod acts as a one-dimensional geometric primitive that represents
    an identifiable extent in time.

    The location in of a gml:TimePeriod is described by the temporal
    positions of the instants at which it begins and ends. The length of
    the period is equal to the temporal distance between the two
    bounding temporal positions. Both beginning and end may be described
    in terms of their direct position using gml:TimePositionType which
    is an XML Schema simple content type, or by reference to an
    indentifiable time instant using gml:TimeInstantPropertyType.
    Alternatively a limit of a gml:TimePeriod may use the conventional
    GML property model to make a reference to a time instant described
    elsewhere, or a limit may be indicated as a direct position.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimePeriodPropertyType:
    """
    Gml:TimePeriodPropertyType provides for associating a gml:TimePeriod with an
    object.
    """
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
