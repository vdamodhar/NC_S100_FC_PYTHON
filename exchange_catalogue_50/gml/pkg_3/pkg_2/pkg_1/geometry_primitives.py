from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union, Any
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    NilReasonEnumerationValue,
    SignType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import (
    Coordinates,
    PointRep,
    PolygonPatches,
    TrianglePatches,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    AbstractCurveType,
    AbstractGeometricPrimitiveType,
    CurvePropertyType,
    DirectPositionType,
    VectorType,
    PointProperty,
    Pos,
    PosList,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import (
    AbstractRingType,
    AbstractSurfaceType,
    SurfacePropertyType,
    Exterior,
    Interior,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_complexes import CompositeSolid
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import AggregationType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.measures import (
    AngleType,
    LengthType,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCurveSegmentType:
    num_derivatives_at_start: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtStart",
            "type": "Attribute",
        }
    )
    num_derivatives_at_end: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtEnd",
            "type": "Attribute",
        }
    )
    num_derivative_interior: int = field(
        default=0,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractSurfacePatchType:
    pass


class CurveInterpolationType(Enum):
    """
    Gml:CurveInterpolationType is a list of codes that may be used to identify the
    interpolation mechanisms specified by an application schema.
    """
    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    CIRCULAR_ARC2_POINT_WITH_BULGE = "circularArc2PointWithBulge"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    ELLIPTICAL = "elliptical"
    CLOTHOID = "clothoid"
    CONIC = "conic"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"


@dataclass
class KnotType:
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    multiplicity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


class KnotTypesType(Enum):
    """
    This enumeration type specifies values for the knots' type (see ISO 19107:2003,
    6.4.25).
    """
    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"


class SurfaceInterpolationType(Enum):
    """
    Gml:SurfaceInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an application schema.
    """
    NONE = "none"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    TIN = "tin"
    PARAMETRIC_CURVE = "parametricCurve"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    RATIONAL_SPLINE = "rationalSpline"
    TRIANGULATED_SPLINE = "triangulatedSpline"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """Gml:AbstractSolidType is an abstraction of a solid to support the different
    levels of complexity.

    The solid may always be viewed as a geometric primitive, i.e. is
    contiguous.
    """


@dataclass
class AffinePlacementType:
    location: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    ref_direction: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    in_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "inDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    out_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "outDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class ArcByCenterPointType(AbstractCurveSegmentType):
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: Optional[PointRep] = field(
        default=None,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    radius: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    start_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    end_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "endAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ArcStringByBulgeType(AbstractCurveSegmentType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    bulge: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    normal: List[VectorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC2_POINT_WITH_BULGE,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class ArcStringType(AbstractCurveSegmentType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class CubicSplineType(AbstractCurveSegmentType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vector_at_start: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "vectorAtStart",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    vector_at_end: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "vectorAtEnd",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CUBIC_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    degree: int = field(
        init=False,
        default=3,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeodesicStringType(AbstractCurveSegmentType):
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class KnotPropertyType:
    """
    Gml:KnotPropertyType encapsulates a knot to use it in a geometric type.

    :ivar knot: A knot is a breakpoint on a piecewise spline curve.
        value is the value of the parameter at the knot of the spline
        (see ISO 19107:2003, 6.4.24.2). multiplicity is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight). weight is the value of the averaging weight used for
        this knot of the spline.
    """
    knot: Optional[KnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class LineStringSegmentType(AbstractCurveSegmentType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class OffsetCurveType(AbstractCurveSegmentType):
    offset_base: Optional["CurvePropertyType"] = field(
        default=None,
        metadata={
            "name": "offsetBase",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    distance: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    ref_direction: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class OrientableCurveType(AbstractCurveType):
    base_curve: Optional["BaseCurve"] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    base_surface: Optional["BaseSurface"] = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RectangleType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TriangleType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BaseCurve(CurvePropertyType):
    """The property baseCurve references or contains the base curve, i.e. it either
    references the base curve via the XLink-attributes or contains the curve
    element.

    A curve element is any element which is substitutable for
    AbstractCurve. The base curve has positive orientation.
    """
    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseSurface(SurfacePropertyType):
    """The property baseSurface references or contains the base surface.

    The property baseSurface either references the base surface via the
    XLink-attributes or contains the surface element. A surface element
    is any element which is substitutable for gml:AbstractSurface. The
    base surface has positive orientation.
    """
    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveMember(CurvePropertyType):
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element, which is substitutable for
    gml:AbstractSurface.
    """
    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    rows: Optional["AbstractGriddedSurfaceType.Rows"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    rows_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "rows",
            "type": "Attribute",
        }
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Rows:
        row: List["AbstractGriddedSurfaceType.Rows.Row"] = field(
            default_factory=list,
            metadata={
                "name": "Row",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Row:
            pos_list: Optional[PosList] = field(
                default=None,
                metadata={
                    "name": "posList",
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml/3.2",
                }
            )
            pos: List[Pos] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml/3.2",
                }
            )
            point_property: List[PointProperty] = field(
                default_factory=list,
                metadata={
                    "name": "pointProperty",
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml/3.2",
                }
            )


@dataclass
class AffinePlacement(AffinePlacementType):
    """
    Location, refDirection, inDimension and outDimension have the same meaning as
    specified in ISO 19107:2003, 6.4.21.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByBulgeType(ArcStringByBulgeType):
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class ArcByCenterPoint(ArcByCenterPointType):
    """This variant of the arc requires that the points on the arc shall be
    computed instead of storing the coordinates directly.

    The single control point is the center point of the arc plus the
    radius and the bearing at start and end. This representation can be
    used only in 2D. The element radius specifies the radius of the arc.
    The element startAngle specifies the bearing of the arc at the
    start. The element endAngle specifies the bearing of the arc at the
    end. The interpolation is fixed as
    "circularArcCenterPointWithRadius". Since this type describes always
    a single arc, the attribute "numArc" is fixed to "1". The content
    model follows the general pattern for the encoding of curve
    segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcString(ArcStringType):
    """An ArcString is a curve segment that uses three-point circular arc
    interpolation ("circularArc3Points").

    The number of arcs in the arc string may be explicitly stated in the
    attribute numArc. The number of control points in the arc string
    shall be 2 * numArc + 1. The content model follows the general
    pattern for the encoding of curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcStringByBulge(ArcStringByBulgeType):
    """This variant of the arc computes the mid points of the arcs instead of
    storing the coordinates directly.

    The control point sequence consists of the start and end points of
    each arc plus the bulge (see ISO 19107:2003, 6.4.17.2). The normal
    is a vector normal (perpendicular) to the chord of the arc (see ISO
    19107:2003, 6.4.17.4). The interpolation is fixed as
    "circularArc2PointWithBulge". The number of arcs in the arc string
    may be explicitly stated in the attribute numArc. The number of
    control points in the arc string shall be numArc + 1. The content
    model follows the general pattern for the encoding of curve
    segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcType(ArcStringType):
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class BsplineType(AbstractCurveSegmentType):
    class Meta:
        name = "BSplineType"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    knot: List[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
        }
    )
    interpolation: CurveInterpolationType = field(
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    is_polynomial: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        }
    )
    knot_type: Optional[KnotTypesType] = field(
        default=None,
        metadata={
            "name": "knotType",
            "type": "Attribute",
        }
    )


@dataclass
class CircleByCenterPointType(ArcByCenterPointType):
    pass


@dataclass
class CubicSpline(CubicSplineType):
    """The number of control points shall be at least three.

    vectorAtStart is the unit tangent vector at the start point of the
    spline. vectorAtEnd is the unit tangent vector at the end point of
    the spline. Only the direction of the vectors shall be used to
    determine the shape of the cubic spline, not their length.
    interpolation is fixed as "cubicSpline". degree shall be the degree
    of the polynomial used for the interpolation in this spline.
    Therefore the degree for a cubic spline is fixed to "3". The content
    model follows the general pattern for the encoding of curve
    segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodesicString(GeodesicStringType):
    """A sequence of geodesic segments.

    The number of control points shall be at least two. interpolation is
    fixed as "geodesic". The content model follows the general pattern
    for the encoding of curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodesicType(GeodesicStringType):
    pass


@dataclass
class LineStringSegment(LineStringSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    control points including the start and end point, with linear interpolation
    between them.

    The content model follows the general pattern for the encoding of
    curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OffsetCurve(OffsetCurveType):
    """An offset curve is a curve at a constant distance from the basis curve.

    offsetBase is the base curve from which this curve is defined as an
    offset. distance and refDirection have the same meaning as specified
    in ISO 19107:2003, 6.4.23. The content model follows the general
    pattern for the encoding of curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableCurve(OrientableCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another AbstractCurve with a parameterization that
    reverses the sense of the curve traversal.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a gml:AbstractSurface with an
    up-normal that reverses the direction for this OrientableSurface,
    the sense of "the top of the surface".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonPatch(PolygonPatchType):
    """A gml:PolygonPatch is a surface patch that is defined by a set of boundary
    curves and an underlying surface to which these curves adhere.

    The curves shall be coplanar and the polygon uses planar
    interpolation in its interior. interpolation is fixed to "planar",
    i.e. an interpolation shall return points on a single plane. The
    boundary of the patch shall be contained within that plane.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Rectangle(RectangleType):
    """Gml:Rectangle represents a rectangle as a surface patch with an outer
    boundary consisting of a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring shall be five. The ring (element
    exterior) shall be a gml:LinearRing and shall form a rectangle; the
    first and the last position shall be coincident. interpolation is
    fixed to "planar", i.e. an interpolation shall return points on a
    single plane. The boundary of the patch shall be contained within
    that plane.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RingType(AbstractRingType):
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class ShellType(AbstractSurfaceType):
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class Triangle(TriangleType):
    """Gml:Triangle represents a triangle as a surface patch with an outer boundary
    consisting of a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring shall be four. The ring (element
    exterior) shall be a gml:LinearRing and shall form a triangle, the
    first and the last position shall be coincident. interpolation is
    fixed to "planar", i.e. an interpolation shall return points on a
    single plane. The boundary of the patch shall be contained within
    that plane.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Arc(ArcType):
    """An Arc is an arc string with only one arc unit, i.e. three control points
    including the start and end point.

    As arc is an arc string consisting of a single arc, the attribute
    "numArc" is fixed to "1".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByBulge(ArcByBulgeType):
    """An ArcByBulge is an arc string with only one arc unit, i.e. two control
    points, one bulge and one normal vector.

    As arc is an arc string consisting of a single arc, the attribute
    "numArc" is fixed to "1".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Bspline(BsplineType):
    """A B-Spline is a piecewise parametric polynomial or rational curve described
    in terms of control points and basis functions as specified in ISO 19107:2003,
    6.4.30.

    Therefore, interpolation may be either "polynomialSpline" or
    "rationalSpline" depending on the interpolation type; default is
    "polynomialSpline". degree shall be the degree of the polynomial
    used for interpolation in this spline. knot shall be the sequence of
    distinct knots used to define the spline basis functions (see ISO
    19107:2003, 6.4.26.2). The attribute isPolynomial shall be set to
    "true" if this is a polynomial spline (see ISO 19107:2003,
    6.4.30.5). The attribute knotType shall provide the type of knot
    distribution used in defining this spline (see ISO 19107:2003,
    6.4.30.4). The content model follows the general pattern for the
    encoding of curve segments.
    """
    class Meta:
        name = "BSpline"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BezierType(BsplineType):
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    is_polynomial: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        }
    )
    knot_type: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        }
    )


@dataclass
class CircleByCenterPoint(CircleByCenterPointType):
    """A gml:CircleByCenterPoint is an gml:ArcByCenterPoint with identical start
    and end angle to form a full circle.

    Again, this representation can be used only in 2D.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CircleType(ArcType):
    pass


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    ref_location: Optional["ClothoidType.RefLocation"] = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    scale_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    start_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    end_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CLOTHOID,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class RefLocation:
        affine_placement: Optional[AffinePlacement] = field(
            default=None,
            metadata={
                "name": "AffinePlacement",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
                "required": True,
            }
        )


@dataclass
class ConeType(AbstractGriddedSurfaceType):
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class CylinderType(AbstractGriddedSurfaceType):
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringSegmentArrayPropertyType:
    """
    Gml:LineStringSegmentArrayPropertyType provides a container for line strings.
    """
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class Ring(RingType):
    """A ring is used to represent a single connected component of a surface
    boundary as specified in ISO 19107:2003, 6.3.6.

    Every gml:curveMember references or contains one curve, i.e. any
    element which is substitutable for gml:AbstractCurve. In the context
    of a ring, the curves describe the boundary of the surface. The
    sequence of curves shall be contiguous and connected in a cycle. If
    provided, the aggregationType attribute shall have the value
    "sequence".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Shell(ShellType):
    """A shell is used to represent a single connected component of a solid
    boundary as specified in ISO 19107:2003, 6.3.8.

    Every gml:surfaceMember references or contains one surface, i.e. any
    element which is substitutable for gml:AbstractSurface. In the
    context of a shell, the surfaces describe the boundary of the solid.
    If provided, the aggregationType attribute shall have the value
    "set".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SphereType(AbstractGriddedSurfaceType):
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class Bezier(BezierType):
    """Bezier curves are polynomial splines that use Bezier or Bernstein
    polynomials for interpolation purposes.

    It is a special case of the B-Spline curve with two knots. degree
    shall be the degree of the polynomial used for interpolation in this
    spline. knot shall be the sequence of distinct knots used to define
    the spline basis functions. interpolation is fixed as
    "polynomialSpline". isPolynomial is fixed as "true". knotType is not
    relevant for Bezier curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Circle(CircleType):
    """A Circle is an arc whose ends coincide to form a simple closed loop.

    The three control points shall be distinct non-co-linear points for
    the circle to be unambiguously defined. The arc is simply extended
    past the third control point until the first control point is
    encountered.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Clothoid(ClothoidType):
    """A clothoid, or Cornu's spiral, is plane curve whose curvature is a fixed
    function of its length.

    refLocation, startParameter, endParameter and scaleFactor have the
    same meaning as specified in ISO 19107:2003, 6.4.22. interpolation
    is fixed as "clothoid". The content model follows the general
    pattern for the encoding of curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RingPropertyType:
    """
    A property with the content model of gml:RingPropertyType encapsulates a ring
    to represent a component of a surface boundary.
    """
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class ShellPropertyType:
    """
    A property with the content model of gml:ShellPropertyType encapsulates a shell
    to represent a component of a solid boundary.
    """
    shell: Optional[Shell] = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveSegmentArrayPropertyType:
    """
    Gml:CurveSegmentArrayPropertyType is a container for an array of curve
    segments.
    """
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    clothoid: List[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    offset_curve: List[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    bezier: List[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    bspline: List[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    cubic_spline: List[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    circle_by_center_point: List[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    arc_by_center_point: List[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    arc_by_bulge: List[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    arc_string_by_bulge: List[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    circle: List[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    arc: List[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    arc_string: List[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )


@dataclass
class SolidType(AbstractSolidType):
    exterior: Optional[ShellPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interior: List[ShellPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class SurfacePatchArrayPropertyType:
    """
    Gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """
    sphere: List[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    cylinder: List[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    cone: List[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    rectangle: List[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    triangle: List[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )


@dataclass
class Solid(SolidType):
    """A solid is the basis for 3-dimensional geometry.

    The extent of a solid is defined by the boundary surfaces as
    specified in ISO 19107:2003, 6.3.18. exterior specifies the outer
    boundary, interior the inner boundary of the solid.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """The patches property element contains the sequence of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveType(AbstractCurveType):
    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class SolidArrayPropertyType:
    """Gml:SolidArrayPropertyType is a container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    solid: List[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SolidPropertyType:
    """A property that has a solid as its value domain may either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    composite_solid: Optional["CompositeSolid"] = field(
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
class SurfaceType(AbstractSurfaceType):
    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon_patches: Optional[PolygonPatches] = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class Curve(CurveType):
    """A curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive. The element segments
    encapsulates the segments of the curve.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolyhedralSurface(SurfaceType):
    """A polyhedral surface is a surface composed of polygon patches connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable. polygonPatches encapsulates the
    polygon patches of the polyhedral surface.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Surface(SurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TinType(SurfaceType):
    stop_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    break_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    max_length: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    control_point: Optional["TinType.ControlPoint"] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )

    @dataclass
    class ControlPoint:
        pos_list: Optional[PosList] = field(
            default=None,
            metadata={
                "name": "posList",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            }
        )
        pos: List[Pos] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            }
        )
        point_property: List[PointProperty] = field(
            default_factory=list,
            metadata={
                "name": "pointProperty",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            }
        )


@dataclass
class TriangulatedSurface(SurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    trianglePatches encapsulates the triangles of the triangulated
    surface.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidProperty(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes or
    contains the solid element.

    solidProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for AbstractSolid.
    """
    class Meta:
        name = "solidProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Tin(TinType):
    """A tin is a triangulated surface that uses the Delauny algorithm or a similar
    algorithm complemented with consideration of stoplines (stopLines), breaklines
    (breakLines), and maximum length of triangle sides (maxLength).

    controlPoint shall contain a set of the positions (three or more)
    used as posts for this TIN (corners of the triangles in the TIN).
    See ISO 19107:2003, 6.4.39 for details.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
