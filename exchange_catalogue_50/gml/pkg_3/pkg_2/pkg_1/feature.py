from dataclasses import dataclass, field
from typing import Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    CodeType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coverage import (
    GridCoverage,
    MultiCurveCoverage,
    MultiPointCoverage,
    MultiSolidCoverage,
    MultiSurfaceCoverage,
    RectifiedGridCoverage,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import (
    FeatureCollection,
    Location,
    PriorityLocation,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.dynamic_feature import (
    DynamicFeature,
    DynamicFeatureCollection,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    Envelope,
    EnvelopeType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import (
    AbstractGmltype,
    ReferenceType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.observation import (
    DirectedObservation,
    DirectedObservationAtDistance,
    Observation,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal import TimePositionType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureMemberType:
    """To create a collection of GML features, a property type shall be derived by
    extension from gml:AbstractFeatureMemberType.

    By default, this abstract property type does not imply any ownership
    of the features in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of a feature in the collection. A
    collection shall not own a feature already owned by another object.
    """
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EnvelopeWithTimePeriodType(EnvelopeType):
    begin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    end_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FeaturePropertyType:
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_observation_at_distance: Optional[DirectedObservationAtDistance] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_observation: Optional[DirectedObservation] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
class LocationName(CodeType):
    """The gml:locationName property element is a convenience property where the
    text value describes the location of the feature.

    If the location names are selected from a controlled list, then the
    list shall be identified in the codeSpace attribute.
    """
    class Meta:
        name = "locationName"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationReference(ReferenceType):
    """
    The gml:locationReference property element is a convenience property where the
    text value referenced by the xlink:href attribute describes the location of the
    feature.
    """
    class Meta:
        name = "locationReference"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EnvelopeWithTimePeriod(EnvelopeWithTimePeriodType):
    """Gml:EnvelopeWithTimePeriod is provided for envelopes that include a temporal
    extent.

    It adds two time position properties, gml:beginPosition and
    gml:endPosition, which describe the extent of a time-envelope. Since
    gml:EnvelopeWithTimePeriod is assigned to the substitution group
    headed by gml:Envelope, it may be used whenever gml:Envelope is
    valid.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundingShapeType:
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    null: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "pattern": r"other:\w{2,}",
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


@dataclass
class BoundedBy(BoundingShapeType):
    """
    This property describes the minimum bounding box or rectangle that encloses the
    entire feature.
    """
    class Meta:
        name = "boundedBy"
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureType(AbstractGmltype):
    """The basic feature model is given by the gml:AbstractFeatureType.

    The content model for gml:AbstractFeatureType adds two specific
    properties suitable for geographic features to the content model
    defined in gml:AbstractGMLType. The value of the gml:boundedBy
    property describes an envelope that encloses the entire feature
    instance, and is primarily useful for supporting rapid searching for
    features that occur in a particular location. The value of the
    gml:location property describes the extent, position or relative
    location of the feature.
    """
    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )
    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
