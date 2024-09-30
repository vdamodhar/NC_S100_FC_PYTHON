from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    CodeType,
    CoordinatesType,
    MeasureType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coordinate_operations import (
    AbstractGeneralOperationParameterPropertyType,
    AbstractGeneralParameterValuePropertyType,
    ConcatenatedOperation,
    ConcatenatedOperationPropertyType,
    ConversionPropertyType,
    Conversion1,
    CoordinateOperationPropertyType,
    GeneralConversionPropertyType,
    GeneralTransformationPropertyType,
    OperationMethod,
    OperationMethodPropertyType,
    OperationParameterGroup,
    OperationParameterGroupPropertyType,
    OperationParameterPropertyType,
    OperationParameter1,
    ParameterValueGroup,
    ParameterValue1,
    PassThroughOperation,
    PassThroughOperationPropertyType,
    SingleOperationPropertyType,
    Transformation,
    TransformationPropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coordinate_reference_systems import (
    CompoundCrs,
    CompoundCrspropertyType,
    DerivedCrs,
    DerivedCrspropertyType,
    EngineeringCrs,
    EngineeringCrspropertyType,
    GeodeticCrs,
    ImageCrs,
    ImageCrspropertyType,
    ProjectedCrs,
    ProjectedCrspropertyType,
    SingleCrspropertyType,
    TemporalCrs,
    TemporalCrspropertyType,
    VerticalCrs,
    VerticalCrspropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coordinate_systems import (
    AbstractCoordinateSystemType,
    AffineCspropertyType,
    AffineCs1,
    CartesianCspropertyType,
    CartesianCs1,
    CoordinateSystemAxis,
    CoordinateSystemAxisPropertyType,
    CoordinateSystemPropertyType,
    CylindricalCspropertyType,
    CylindricalCs1,
    EllipsoidalCspropertyType,
    EllipsoidalCs1,
    LinearCspropertyType,
    LinearCs1,
    PolarCspropertyType,
    PolarCs1,
    SphericalCspropertyType,
    SphericalCs1,
    TimeCspropertyType,
    TimeCs1,
    UserDefinedCspropertyType,
    UserDefinedCs1,
    VerticalCspropertyType,
    VerticalCs1,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coverage import (
    CoverageMappingRule,
    DataBlock,
    DomainSetType,
    File,
    GridCoverage,
    GridFunction,
    MultiCurveCoverage,
    MultiPointCoverage,
    MultiSolidCoverage,
    MultiSurfaceCoverage,
    RectifiedGridCoverage,
    CoverageFunction,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.datums import (
    DatumPropertyType,
    EllipsoidPropertyType,
    Ellipsoid1,
    EngineeringDatumPropertyType,
    EngineeringDatum1,
    GeodeticDatumPropertyType,
    GeodeticDatum1,
    ImageDatumPropertyType,
    ImageDatum1,
    PrimeMeridianPropertyType,
    PrimeMeridian1,
    TemporalDatumPropertyType,
    TemporalDatum1,
    VerticalDatumPropertyType,
    VerticalDatum1,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.dictionary import (
    Definition,
    DefinitionType,
    Dictionary,
    DictionaryEntryType,
    DictionaryType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.direction import DirectionPropertyType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.dynamic_feature import (
    AbstractTimeSliceType,
    DynamicFeature,
    DynamicFeatureCollection,
    HistoryPropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.feature import (
    AbstractFeatureType,
    EnvelopeWithTimePeriod,
    FeaturePropertyType,
    BoundedBy,
    LocationName,
    LocationReference,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_aggregates import (
    MultiCurve,
    MultiCurvePropertyType,
    MultiGeometry,
    MultiGeometryPropertyType,
    MultiPoint,
    MultiPointPropertyType,
    MultiSolid,
    MultiSolidPropertyType,
    MultiSurface,
    MultiSurfacePropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    CurveArrayPropertyType,
    CurvePropertyType,
    Envelope,
    GeometryPropertyType,
    LineString,
    Point,
    PointArrayPropertyType,
    PointPropertyType,
    Pos,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import (
    LinearRing,
    Polygon,
    SurfaceArrayPropertyType,
    SurfacePropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_complexes import (
    CompositeCurve,
    CompositeSolid,
    CompositeSurface,
    GeometricComplex,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_primitives import (
    AffinePlacement,
    Arc,
    ArcByBulge,
    ArcByCenterPoint,
    ArcString,
    ArcStringByBulge,
    Bspline,
    Bezier,
    Circle,
    CircleByCenterPoint,
    Clothoid,
    CubicSpline,
    Curve,
    Geodesic,
    GeodesicString,
    LineStringSegment,
    OffsetCurve,
    OrientableCurve,
    OrientableSurface,
    PolyhedralSurface,
    Ring,
    Shell,
    Solid,
    SolidArrayPropertyType,
    Surface,
    SurfacePatchArrayPropertyType,
    Tin,
    TriangulatedSurface,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import (
    AbstractGmltype,
    AssociationRoleType,
    ReferenceType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.grids import (
    Grid,
    RectifiedGrid,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.measures import Angle
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.observation import (
    DirectedObservation,
    DirectedObservationAtDistance,
    Observation,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.reference_systems import (
    AbstractCrstype,
    CrspropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal import (
    TimeInstant,
    TimePeriod,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal_reference_systems import (
    TimeCalendar,
    TimeClock,
    TimeCoordinateSystem,
    TimeOrdinalReferenceSystem,
    TimeReferenceSystem,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal_topology import (
    TimeEdge,
    TimeNode,
    TimeTopologyComplex,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.topology import (
    Edge,
    Face,
    Node,
    TopoComplex,
    TopoComplexPropertyType,
    TopoSolid,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.units import (
    BaseUnit,
    ConventionalUnit,
    DerivedUnit,
    UnitDefinition,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.value_objects import (
    Boolean,
    Category,
    CategoryExtent,
    CategoryList,
    CompositeValue,
    Count,
    Quantity,
    QuantityExtent,
    QuantityList,
    ValueArray,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractMetaDataType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


class DegreesTypeDirection(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"
    VALUE = "+"
    VALUE_1 = "-"


class IncrementOrder(Enum):
    X_Y = "+x+y"
    Y_X = "+y+x"
    X_Y_1 = "+x-y"
    X_Y_2 = "-x-y"


@dataclass
class DecimalMinutes:
    class Meta:
        name = "decimalMinutes"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class Minutes:
    class Meta:
        name = "minutes"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 59,
        }
    )


@dataclass
class Seconds:
    class Meta:
        name = "seconds"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class ArrayType(AbstractGmltype):
    members: Optional["Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )


@dataclass
class DefinitionCollection(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DegreesType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 359,
        }
    )
    direction: Optional[DegreesTypeDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FeatureArrayPropertyType:
    feature_collection: List["FeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    directed_observation_at_distance: List[DirectedObservationAtDistance] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    directed_observation: List[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    observation: List[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    rectified_grid_coverage: List[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    grid_coverage: List[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    multi_solid_coverage: List[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    multi_surface_coverage: List[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    multi_curve_coverage: List[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    multi_point_coverage: List[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    dynamic_feature_collection: List[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    dynamic_feature: List[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )


@dataclass
class GenericMetaDataType(AbstractMetaDataType):
    pass


@dataclass
class GeographicCrspropertyType:
    class Meta:
        name = "GeographicCRSPropertyType"

    geographic_crs: Optional["GeographicCrs"] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
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
class LocationKeyWord(CodeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    value: Union[str, NilReasonEnumerationValue] = field(
        default="",
        metadata={
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ObliqueCartesianCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "ObliqueCartesianCSType"


@dataclass
class OperationPropertyType:
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    conversion: Optional[Conversion1] = field(
        default=None,
        metadata={
            "name": "Conversion",
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
class StringOrRefType:
    value: str = field(
        default="",
        metadata={
            "required": True,
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
class TemporalCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "TemporalCSType"


@dataclass
class AbstractGeneralOperationParameterRef(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "abstractGeneralOperationParameterRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AnchorPoint(CodeType):
    class Meta:
        name = "anchorPoint"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CartesianCsref(CartesianCspropertyType):
    class Meta:
        name = "cartesianCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CenterLineOf(CurvePropertyType):
    class Meta:
        name = "centerLineOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CenterOf(PointPropertyType):
    class Meta:
        name = "centerOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompoundCrsref(CompoundCrspropertyType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ConcatenatedOperationRef(ConcatenatedOperationPropertyType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ConversionRef(ConversionPropertyType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateOperationRef(CoordinateOperationPropertyType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemAxisRef(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "coordinateSystemAxisRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemRef(CoordinateSystemPropertyType):
    class Meta:
        name = "coordinateSystemRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Coordinates(CoordinatesType):
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CrsRef(CrspropertyType):
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveArrayProperty(CurveArrayPropertyType):
    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCsref(CylindricalCspropertyType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DatumRef(DatumPropertyType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinedByConversion(GeneralConversionPropertyType):
    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionMember(DictionaryEntryType):
    class Meta:
        name = "definitionMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionRef(ReferenceType):
    class Meta:
        name = "definitionRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrsref(DerivedCrspropertyType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EdgeOf(CurvePropertyType):
    class Meta:
        name = "edgeOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidRef(EllipsoidPropertyType):
    class Meta:
        name = "ellipsoidRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidalCsref(EllipsoidalCspropertyType):
    class Meta:
        name = "ellipsoidalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrsref(EngineeringCrspropertyType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringDatumRef(EngineeringDatumPropertyType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureMember(FeaturePropertyType):
    class Meta:
        name = "featureMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralConversionRef(GeneralConversionPropertyType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "generalOperationParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralTransformationRef(GeneralTransformationPropertyType):
    class Meta:
        name = "generalTransformationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatumRef(GeodeticDatumPropertyType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GridDomain(DomainSetType):
    class Meta:
        name = "gridDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageCrsref(ImageCrspropertyType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatumRef(ImageDatumPropertyType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IncludesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "includesParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IncludesSingleCrs(SingleCrspropertyType):
    class Meta:
        name = "includesSingleCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IncludesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "includesValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearCsref(LinearCspropertyType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Member(AssociationRoleType):
    class Meta:
        name = "member"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MethodFormula(CodeType):
    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCenterLineOf(MultiCurvePropertyType):
    class Meta:
        name = "multiCenterLineOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCenterOf(MultiPointPropertyType):
    class Meta:
        name = "multiCenterOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCoverage(MultiSurfacePropertyType):
    class Meta:
        name = "multiCoverage"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveDomain(DomainSetType):
    class Meta:
        name = "multiCurveDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveProperty(MultiCurvePropertyType):
    class Meta:
        name = "multiCurveProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiEdgeOf(MultiCurvePropertyType):
    class Meta:
        name = "multiEdgeOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiExtentOf(MultiSurfacePropertyType):
    class Meta:
        name = "multiExtentOf"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiLocation(MultiPointPropertyType):
    class Meta:
        name = "multiLocation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointDomain(DomainSetType):
    class Meta:
        name = "multiPointDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPosition(MultiPointPropertyType):
    class Meta:
        name = "multiPosition"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidDomain(DomainSetType):
    class Meta:
        name = "multiSolidDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidProperty(MultiSolidPropertyType):
    class Meta:
        name = "multiSolidProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfaceDomain(DomainSetType):
    class Meta:
        name = "multiSurfaceDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfaceProperty(MultiSurfacePropertyType):
    class Meta:
        name = "multiSurfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationMethodRef(OperationMethodPropertyType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameterGroupRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterGroupRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameterRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PassThroughOperationRef(PassThroughOperationPropertyType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayProperty(PointArrayPropertyType):
    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointRep(PointPropertyType):
    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolarCsref(PolarCspropertyType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonPatches(SurfacePatchArrayPropertyType):
    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Position(PointPropertyType):
    class Meta:
        name = "position"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PrimeMeridianRef(PrimeMeridianPropertyType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ProjectedCrsref(ProjectedCrspropertyType):
    class Meta:
        name = "projectedCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RectifiedGridDomain(DomainSetType):
    class Meta:
        name = "rectifiedGridDomain"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ReferenceSystemRef(CrspropertyType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SingleCrsref(SingleCrspropertyType):
    class Meta:
        name = "singleCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SingleOperationRef(SingleOperationPropertyType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidArrayProperty(SolidArrayPropertyType):
    class Meta:
        name = "solidArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SphericalCsref(SphericalCspropertyType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class StatusReference(ReferenceType):
    class Meta:
        name = "statusReference"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceArrayProperty(SurfaceArrayPropertyType):
    class Meta:
        name = "surfaceArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCrsref(TemporalCrspropertyType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalDatumRef(TemporalDatumPropertyType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexProperty(TopoComplexPropertyType):
    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Track(HistoryPropertyType):
    class Meta:
        name = "track"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TransformationRef(TransformationPropertyType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TrianglePatches(SurfacePatchArrayPropertyType):
    class Meta:
        name = "trianglePatches"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCsref(UserDefinedCspropertyType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesAffineCs(AffineCspropertyType):
    class Meta:
        name = "usesAffineCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesAxis(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "usesAxis"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesCs(CoordinateSystemPropertyType):
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesCartesianCs(CartesianCspropertyType):
    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEllipsoid(EllipsoidPropertyType):
    class Meta:
        name = "usesEllipsoid"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEllipsoidalCs(EllipsoidalCspropertyType):
    class Meta:
        name = "usesEllipsoidalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEngineeringDatum(EngineeringDatumPropertyType):
    class Meta:
        name = "usesEngineeringDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesGeodeticDatum(GeodeticDatumPropertyType):
    class Meta:
        name = "usesGeodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesImageDatum(ImageDatumPropertyType):
    class Meta:
        name = "usesImageDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesMethod(OperationMethodPropertyType):
    class Meta:
        name = "usesMethod"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesOperation(CoordinateOperationPropertyType):
    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesPrimeMeridian(PrimeMeridianPropertyType):
    class Meta:
        name = "usesPrimeMeridian"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesSingleOperation(CoordinateOperationPropertyType):
    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesSphericalCs(SphericalCspropertyType):
    class Meta:
        name = "usesSphericalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTemporalDatum(TemporalDatumPropertyType):
    class Meta:
        name = "usesTemporalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTimeCs(TimeCspropertyType):
    class Meta:
        name = "usesTimeCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "usesValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesVerticalCs(VerticalCspropertyType):
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesVerticalDatum(VerticalDatumPropertyType):
    class Meta:
        name = "usesVerticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ValueOfParameter(OperationParameterPropertyType):
    class Meta:
        name = "valueOfParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ValuesOfGroup(OperationParameterGroupPropertyType):
    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCrsref(VerticalCrspropertyType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCsref(VerticalCspropertyType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatumRef(VerticalDatumPropertyType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Array(ArrayType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BagType(AbstractGmltype):
    member: List[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    members: Optional["Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DefinitionProxyType(DefinitionType):
    definition_ref: Optional[DefinitionRef] = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class GenericMetaData(GenericMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeocentricCrstype(AbstractCrstype):
    class Meta:
        name = "GeocentricCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class GeographicCrstype(AbstractCrstype):
    class Meta:
        name = "GeographicCRSType"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class LocationString(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MappingRule(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ObliqueCartesianCs(ObliqueCartesianCstype):
    class Meta:
        name = "ObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseGeographicCrs(GeographicCrspropertyType):
    class Meta:
        name = "baseGeographicCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureMembers(FeatureArrayPropertyType):
    class Meta:
        name = "featureMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeographicCrsref(GeographicCrspropertyType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationRef(OperationPropertyType):
    class Meta:
        name = "operationRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Status(StringOrRefType):
    class Meta:
        name = "status"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureCollectionType(AbstractFeatureType):
    feature_member: List["FeatureMember"] = field(
        default_factory=list,
        metadata={
            "name": "featureMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    feature_members: Optional[FeatureMembers] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class Bag(BagType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsangleType:
    class Meta:
        name = "DMSAngleType"

    degrees: Optional[Degrees] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    decimal_minutes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )
    minutes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "max_inclusive": 59,
        }
    )
    seconds: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class DefinitionProxy(DefinitionProxyType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationPropertyType:
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    shell: Optional[Shell] = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    location_key_word: Optional[LocationKeyWord] = field(
        default=None,
        metadata={
            "name": "LocationKeyWord",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    location_string: Optional[LocationString] = field(
        default=None,
        metadata={
            "name": "LocationString",
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
class MetaDataPropertyType:
    generic_meta_data: Optional[GenericMetaData] = field(
        default=None,
        metadata={
            "name": "GenericMetaData",
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
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ObliqueCartesianCspropertyType:
    class Meta:
        name = "ObliqueCartesianCSPropertyType"

    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
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
class TemporalCspropertyType:
    class Meta:
        name = "TemporalCSPropertyType"

    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
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
class FeatureCollectionType(AbstractFeatureCollectionType):
    pass


@dataclass
class GeocentricCrspropertyType:
    class Meta:
        name = "GeocentricCRSPropertyType"

    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
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
class IndirectEntryType:
    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DmsAngle(DmsangleType):
    class Meta:
        name = "dmsAngle"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsAngleValue(DmsangleType):
    class Meta:
        name = "dmsAngleValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Location(LocationPropertyType):
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MetaDataProperty(MetaDataPropertyType):
    class Meta:
        name = "metaDataProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ObliqueCartesianCsref(ObliqueCartesianCspropertyType):
    class Meta:
        name = "obliqueCartesianCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCsref(TemporalCspropertyType):
    class Meta:
        name = "temporalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesObliqueCartesianCs(ObliqueCartesianCspropertyType):
    class Meta:
        name = "usesObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTemporalCs(TemporalCspropertyType):
    class Meta:
        name = "usesTemporalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AngleChoiceType:
    angle: Optional[Angle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dms_angle: Optional[DmsAngle] = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class FeatureCollection(FeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeocentricCrsref(GeocentricCrspropertyType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IndirectEntry(IndirectEntryType):
    class Meta:
        name = "indirectEntry"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PriorityLocation(PriorityLocationPropertyType):
    class Meta:
        name = "priorityLocation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    position: Optional[GeometryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    location_name: Optional[LocationName] = field(
        default=None,
        metadata={
            "name": "locationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    speed: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    bearing: Optional[DirectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    acceleration: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    elevation: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    status_reference: Optional[StatusReference] = field(
        default=None,
        metadata={
            "name": "statusReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArrayAssociationType:
    generic_meta_data: List[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    parameter_value_group: List[ParameterValueGroup] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    parameter_value: List[ParameterValue1] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid_function: List[GridFunction] = field(
        default_factory=list,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coverage_mapping_rule: List[CoverageMappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coverage_function: List[CoverageFunction] = field(
        default_factory=list,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    data_block: List[DataBlock] = field(
        default_factory=list,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    quantity_extent: List[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    count_extent: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_extent: List[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    value_array: List[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_value: List[CompositeValue] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    quantity_list: List[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    count_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_list: List[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    boolean_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    quantity: List[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )
    count: List[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )
    category: List[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )
    boolean: List[Boolean] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )
    affine_placement: List[AffinePlacement] = field(
        default_factory=list,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    clothoid: List[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    offset_curve: List[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    bezier: List[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    bspline: List[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cubic_spline: List[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    circle_by_center_point: List[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    arc_by_center_point: List[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    arc_by_bulge: List[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    arc_string_by_bulge: List[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    circle: List[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    arc: List[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    arc_string: List[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    envelope_with_time_period: List[EnvelopeWithTimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    envelope: List[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    bag: List[Bag] = field(
        default_factory=list,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    topo_complex: List[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    topo_solid: List[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    face: List[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    node: List[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    moving_object_status: List[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    feature_collection: List[FeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_observation_at_distance: List[DirectedObservationAtDistance] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_observation: List[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    observation: List[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    rectified_grid_coverage: List[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid_coverage: List[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_solid_coverage: List[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_surface_coverage: List[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_curve_coverage: List[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_point_coverage: List[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dynamic_feature_collection: List[DynamicFeatureCollection] = field(
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
    time_topology_complex: List[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_edge: List[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_node: List[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_period: List[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_instant: List[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    rectified_grid: List[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid: List[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geometric_complex: List[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_solid: List[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_surface: List[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_curve: List[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_geometry: List[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    solid: List[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    shell: List[Shell] = field(
        default_factory=list,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    surface: List[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: List[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    ring: List[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    linear_ring: List[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    definition_proxy: List[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    definition_collection: List[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_ordinal_reference_system: List[TimeOrdinalReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_clock: List[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_calendar: List[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_coordinate_system: List[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_reference_system: List[TimeReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    operation_parameter_group: List[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    operation_parameter: List[OperationParameter1] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    operation_method: List[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    concatenated_operation: List[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    transformation: List[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    conversion: List[Conversion1] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pass_through_operation: List[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    prime_meridian: List[PrimeMeridian1] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    ellipsoid: List[Ellipsoid1] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    temporal_datum: List[TemporalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_datum: List[VerticalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    image_datum: List[ImageDatum1] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    engineering_datum: List[EngineeringDatum1] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_datum: List[GeodeticDatum1] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    oblique_cartesian_cs: List[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    temporal_cs: List[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    affine_cs: List[AffineCs1] = field(
        default_factory=list,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cylindrical_cs: List[CylindricalCs1] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polar_cs: List[PolarCs1] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    spherical_cs: List[SphericalCs1] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    user_defined_cs: List[UserDefinedCs1] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    linear_cs: List[LinearCs1] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_cs: List[TimeCs1] = field(
        default_factory=list,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_cs: List[VerticalCs1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: List[CartesianCs1] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    ellipsoidal_cs: List[EllipsoidalCs1] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinate_system_axis: List[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    compound_crs: List[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geocentric_crs: List[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geographic_crs: List[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    temporal_crs: List[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    image_crs: List[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    engineering_crs: List[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_crs: List[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_crs: List[GeodeticCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    derived_crs: List[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    projected_crs: List[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    conventional_unit: List[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    derived_unit: List[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    base_unit: List[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    unit_definition: List[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dictionary: List[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    definition: List[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
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
class Members(ArrayAssociationType):
    class Meta:
        name = "members"
        namespace = "http://www.opengis.net/gml/3.2"
