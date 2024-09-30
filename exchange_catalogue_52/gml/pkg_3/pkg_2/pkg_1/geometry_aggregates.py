from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    AbstractGeometryType,
    CurveArrayPropertyType,
    GeometryArrayPropertyType,
    GeometryPropertyType,
    PointArrayPropertyType,
    PointPropertyType,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import SurfaceArrayPropertyType
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.geometry_primitives import (
    SolidArrayPropertyType,
    SolidPropertyType,
    CurveMember,
    SurfaceMember,
)
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.gml_base import AggregationType
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class CurveMembers(CurveArrayPropertyType):
    """This property element contains a list of curves.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "curveMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryMember(GeometryPropertyType):
    """
    This property element either references a geometry element via the XLink-
    attributes or contains the geometry element.
    """
    class Meta:
        name = "geometryMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryMembers(GeometryArrayPropertyType):
    """This property element contains a list of geometry elements.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "geometryMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointMember(PointPropertyType):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """
    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointMembers(PointArrayPropertyType):
    """This property element contains a list of points.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "pointMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidMember(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes or
    contains the solid element.

    A solid element is any element, which is substitutable for
    gml:AbstractSolid.
    """
    class Meta:
        name = "solidMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidMembers(SolidArrayPropertyType):
    """This property element contains a list of solids.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "solidMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMembers(SurfaceArrayPropertyType):
    """This property element contains a list of surfaces.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "surfaceMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve_members: Optional[CurveMembers] = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiGeometryType(AbstractGeometricAggregateType):
    geometry_member: List[GeometryMember] = field(
        default_factory=list,
        metadata={
            "name": "geometryMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geometry_members: Optional[GeometryMembers] = field(
        default=None,
        metadata={
            "name": "geometryMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_members: Optional[PointMembers] = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    solid_member: List[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiCurve(MultiCurveType):
    """A gml:MultiCurve is defined by one or more gml:AbstractCurves.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:curveMember) or the array property
    (gml:curveMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiGeometry(MultiGeometryType):
    """Gml:MultiGeometry is a collection of one or more GML geometry objects of
    arbitrary type.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:geometryMember) or the array property
    (gml:geometryMembers). It is also valid to use both the "standard"
    and the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPoint(MultiPointType):
    """A gml:MultiPoint consists of one or more gml:Points.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:pointMember) or the array property
    (gml:pointMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolid(MultiSolidType):
    """A gml:MultiSolid is defined by one or more gml:AbstractSolids.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:solidMember) or the array property
    (gml:solidMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurface(MultiSurfaceType):
    """A gml:MultiSurface is defined by one or more gml:AbstractSurfaces.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:surfaceMember) or the array property
    (gml:surfaceMembers). It is also valid to use both the "standard"
    and the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurvePropertyType:
    """A property that has a collection of curves as its value domain may either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
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
class MultiGeometryPropertyType:
    """A property that has a geometric aggregate as its value domain may either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
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
class MultiPointPropertyType:
    """A property that has a collection of points as its value domain may either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
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
class MultiSolidPropertyType:
    """A property that has a collection of solids as its value domain may either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
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
class MultiSurfacePropertyType:
    """A property that has a collection of surfaces as its value domain may either
    be an appropriate geometry element encapsulated in an element of this type or
    an XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
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
