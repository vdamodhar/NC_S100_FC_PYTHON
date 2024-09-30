from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_aggregates import SolidMember
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    AbstractCurveType,
    AbstractGeometryType,
    GeometricPrimitivePropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import AbstractSurfaceType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_primitives import AbstractSolidType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import AggregationType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeCurveType(AbstractCurveType):
    curve_member: List["CurveMember"] = field(
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
class CompositeSolidType(AbstractSolidType):
    solid_member: List[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
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
class CompositeSurfaceType(AbstractSurfaceType):
    surface_member: List["SurfaceMember"] = field(
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
class GeometricComplexType(AbstractGeometryType):
    element: List[GeometricPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
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
class CompositeCurve(CompositeCurveType):
    """A gml:CompositeCurve is represented by a sequence of (orientable) curves
    such that each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    curveMember references or contains inline one curve in the composite
    curve. The curves are contiguous, the collection of curves is
    ordered. Therefore, if provided, the aggregationType attribute shall
    have the value "sequence".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeSolid(CompositeSolidType):
    """Gml:CompositeSolid implements ISO 19107 GM_CompositeSolid (see ISO
    19107:2003, 6.6.7) as specified in D.2.3.6.

    A gml:CompositeSolid is represented by a set of orientable surfaces.
    It is a geometry type with all the geometric properties of a
    (primitive) solid. Essentially, a composite solid is a collection of
    solids that join in pairs on common boundary surfaces and which,
    when considered as a whole, form a single solid. solidMember
    references or contains one solid in the composite solid. The solids
    are contiguous.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeSurface(CompositeSurfaceType):
    """A gml:CompositeSurface is represented by a set of orientable surfaces.

    It is geometry type with all the geometric properties of a
    (primitive) surface. Essentially, a composite surface is a
    collection of surfaces that join in pairs on common boundary curves
    and which, when considered as a whole, form a single surface.
    surfaceMember references or contains inline one surface in the
    composite surface. The surfaces are contiguous.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricComplex(GeometricComplexType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricComplexPropertyType:
    """A property that has a geometric complex as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
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
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
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
