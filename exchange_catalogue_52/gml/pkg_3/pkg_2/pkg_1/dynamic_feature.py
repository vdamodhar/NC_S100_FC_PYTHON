from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.deprecated_types import (
    MovingObjectStatus,
    StringOrRefType,
    Track,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.feature import (
    AbstractFeatureMemberType,
    AbstractFeatureType,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.gml_base import (
    AbstractGmltype,
    ReferenceType,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.temporal import ValidTime
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class HistoryPropertyType:
    moving_object_status: List[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
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


@dataclass
class DataSource(StringOrRefType):
    """Evidence is represented by a simple gml:dataSource or
    gml:dataSourceReference property that indicates the source of the temporal
    data.

    The remote link attributes of the gml:dataSource element have been
    deprecated along with its current type.
    """
    class Meta:
        name = "dataSource"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DataSourceReference(ReferenceType):
    """
    Evidence is represented by a simple gml:dataSource or gml:dataSourceReference
    property that indicates the source of the temporal data.
    """
    class Meta:
        name = "dataSourceReference"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class History(HistoryPropertyType):
    """A generic sequence of events constitute a gml:history of an object.

    The gml:history element contains a set of elements in the
    substitution group headed by the abstract element
    gml:AbstractTimeSlice, representing the time-varying properties of
    interest. The history property of a dynamic feature associates a
    feature instance with a sequence of time slices (i.e. change events)
    that encapsulate the evolution of the feature.
    """
    class Meta:
        name = "history"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    data_source_reference: Optional[DataSourceReference] = field(
        default=None,
        metadata={
            "name": "dataSourceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DynamicFeature(DynamicFeatureType):
    """States are captured by time-stamped instances of a feature.

    The content model extends the standard gml:AbstractFeatureType with
    the gml:dynamicProperties model group. Each time-stamped instance
    represents a 'snapshot' of a feature. The dynamic feature classes
    will normally be extended to suit particular applications.  A
    dynamic feature bears either a time stamp or a history.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureMemberType(AbstractFeatureMemberType):
    dynamic_feature_collection: List["DynamicFeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dynamic_feature: List[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
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


@dataclass
class DynamicMembers(DynamicFeatureMemberType):
    class Meta:
        name = "dynamicMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureCollectionType(DynamicFeatureType):
    dynamic_members: Optional[DynamicMembers] = field(
        default=None,
        metadata={
            "name": "dynamicMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class DynamicFeatureCollection(DynamicFeatureCollectionType):
    """A gml:DynamicFeatureCollection is a feature collection that has a
    gml:validTime property (i.e. is a snapshot of the feature collection) or which
    has a gml:history property that contains one or more gml:AbstractTimeSlices
    each of which contain values of the time varying properties of the feature
    collection.

    Note that the gml:DynamicFeatureCollection may be one of the following:
    1.      A feature collection which consists of static feature members (members do not change in time) but which has properties of the collection object as a whole that do change in time .
    2.      A feature collection which consists of dynamic feature members (the members are gml:DynamicFeatures) but which also has properties of the collection as a whole that vary in time.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
