from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    NilReasonEnumerationValue,
    SignType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    CurveProperty,
    PointProperty,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import SurfaceProperty
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_primitives import SolidProperty
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import (
    AbstractGmltype,
    AggregationType,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTopologyType(AbstractGmltype):
    """This abstract type supplies the root or base type for all topological
    elements including primitives and complexes.

    It inherits AbstractGMLType and hence can be identified using the
    gml:id attribute.
    """


@dataclass
class DirectedFacePropertyType:
    face: Optional["Face"] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DirectedNodePropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodePropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
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
class TopoComplexPropertyType:
    topo_complex: Optional["TopoComplex"] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
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
class AbstractTopoPrimitiveType(AbstractTopologyType):
    pass


@dataclass
class DirectedFace(DirectedFacePropertyType):
    """The gml:directedFace property element describes the boundary of topology
    solids, in the coBoundary of topology edges and is used in the support of
    surface features via the gml:TopoSurface expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included face is used i.e. inward or outward with
    respect to the surface normal in any geometric realisation.
    """
    class Meta:
        name = "directedFace"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedNode(DirectedNodePropertyType):
    """A gml:directedNode property element describes the boundary of topology edges
    and is used in the support of topological point features via the gml:TopoPoint
    expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included node is used: start ("-") or end ("+") node.
    """
    class Meta:
        name = "directedNode"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MaximalComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """
    class Meta:
        name = "maximalComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SubComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """
    class Meta:
        name = "subComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SuperComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """
    class Meta:
        name = "superComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointType(AbstractTopologyType):
    directed_node: Optional[DirectedNode] = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class TopoSolidType(AbstractTopoPrimitiveType):
    """
    :ivar isolated:
    :ivar directed_face:
    :ivar solid_property:
    :ivar aggregation_type:
    :ivar universal: A gml:TopoSolid must indicate whether it is a
        universal topo-solid or not, to ensure a lossless topology
        representation as defined by Kuijpers, et. al. (see OGC 05-102
        Topology IPR). The optional universal attribute of type boolean
        is used to indicate this and the default is fault. NOTE The
        universal topo-solid is normally not part of any feature, and is
        used to represent the unbounded portion of the data set. Its
        interior boundary (it has no exterior boundary) would normally
        be considered the exterior boundary of the data set.
    """
    isolated: List["NodeOrEdgePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    solid_property: Optional[SolidProperty] = field(
        default=None,
        metadata={
            "name": "solidProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
    universal: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopoSurfaceType(AbstractTopologyType):
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
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
class TopoPoint(TopoPointType):
    """
    The intended use of gml:TopoPoint is to appear within a point feature to
    express the structural and possibly geometric relationships of this feature to
    other features via shared node definitions.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSolid(TopoSolidType):
    """Gml:TopoSolid represents the 3-dimensional topology primitive.

    The topological boundary of a solid (gml:directedFace) consists of a
    set of directed faces. A solid may optionally be realised by a
    3-dimensional geometric primitive (gml:solidProperty).
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSurface(TopoSurfaceType):
    """Gml:TopoSurface represents a homogeneous topological expression, a set of
    directed faces, which if realised are isomorphic to a geometric surface
    primitive.

    The intended use of gml:TopoSurface is to appear within a surface
    feature to express the structural and possibly geometric
    relationships of this surface feature to other features via the
    shared face definitions.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedTopoSolidPropertyType:
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopoPointPropertyType:
    topo_point: Optional[TopoPoint] = field(
        default=None,
        metadata={
            "name": "TopoPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopoSolidPropertyType:
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
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
class TopoSurfacePropertyType:
    topo_surface: Optional[TopoSurface] = field(
        default=None,
        metadata={
            "name": "TopoSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EdgeType(AbstractTopoPrimitiveType):
    container: Optional[TopoSolidPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_node: List[DirectedNode] = field(
        default_factory=list,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class DirectedTopoSolid(DirectedTopoSolidPropertyType):
    """The gml:directedSolid property element describes the coBoundary of topology
    faces and is used in the support of volume features via the gml:TopoVolume
    expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included solid appears in the face coboundary. In the
    context of a gml:TopoVolume the orientation attribute has no
    meaning.
    """
    class Meta:
        name = "directedTopoSolid"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointProperty(TopoPointPropertyType):
    """
    The gml:topoPointProperty property element may be used in features to express
    their relationship to the referenced topology node.
    """
    class Meta:
        name = "topoPointProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    """
    The gml:topoSurfaceProperty property element may be used in features to express
    their relationship to the referenced topology faces.
    """
    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Edge(EdgeType):
    """Gml:Edge represents the 1-dimensional primitive.

    The topological boundary of an Edge (gml:directedNode) consists of a
    negatively directed start Node and a positively directed end Node.
    The optional coboundary of an edge (gml:directedFace) is a circular
    sequence of directed faces which are incident on this edge in
    document order. In the 2D case, the orientation of the face on the
    left of the edge is "+"; the orientation of the face on the right on
    its right is "-". If provided, the aggregationType attribute shall
    have the value "sequence". An edge may optionally be realised by a
    1-dimensional geometric primitive (gml:curveProperty).
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumeType(AbstractTopologyType):
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
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
class DirectedEdgePropertyType:
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE_1,
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopoVolume(TopoVolumeType):
    """Gml:TopoVolume represents a homogeneous topological expression, a set of
    directed topologic solids, which if realised are isomorphic to a geometric
    solid primitive.

    The intended use of gml:TopoVolume is to appear within a solid
    feature to express the structural and geometric relationships of
    this solid feature to other features via the shared solid
    definitions.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumePropertyType:
    topo_volume: Optional[TopoVolume] = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DirectedEdge(DirectedEdgePropertyType):
    """A gml:directedEdge property element describes the boundary of topology
    faces, the coBoundary of topology nodes and is used in the support of
    topological line features via the gml:TopoCurve expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included edge is used, i.e. forward or reverse.
    """
    class Meta:
        name = "directedEdge"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FaceType(AbstractTopoPrimitiveType):
    """
    :ivar isolated:
    :ivar directed_edge:
    :ivar directed_topo_solid:
    :ivar surface_property:
    :ivar aggregation_type:
    :ivar universal: If the topological representation exists an
        unbounded manifold (e.g. Euclidean plane), a gml:Face must
        indicate whether it is a universal face or not, to ensure a
        lossless topology representation as defined by Kuijpers, et. al.
        (see OGC 05-102 Topology IPR). The optional universal attribute
        of type boolean is used to indicate this. NOTE The universal
        face is normally not part of any feature, and is used to
        represent the unbounded portion of the data set. Its interior
        boundary (it has no exterior boundary) would normally be
        considered the exterior boundary of the map represented by the
        data set.
    """
    isolated: List[NodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "max_occurs": 2,
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
    universal: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopoCurveType(AbstractTopologyType):
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
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
class TopoVolumeProperty(TopoVolumePropertyType):
    """
    The gml:topoVolumeProperty element may be used in features to express their
    relationship to the referenced topology volume.
    """
    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Face(FaceType):
    """Gml:Face represents the 2-dimensional topology primitive.

    The topological boundary of a face (gml:directedEdge) consists of a
    sequence of directed edges. If provided, the aggregationType
    attribute shall have the value "sequence". The optional coboundary
    of a face (gml:directedTopoSolid) is a pair of directed solids which
    are bounded by this face. A positively directed solid corresponds to
    a solid which lies in the direction of the negatively directed
    normal to the face in any geometric realisation. A face may
    optionally be realised by a 2-dimensional geometric primitive
    (gml:surfaceProperty).
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoCurve(TopoCurveType):
    """Gml:TopoCurve represents a homogeneous topological expression, a sequence of
    directed edges, which if realised are isomorphic to a geometric curve
    primitive.

    The intended use of gml:TopoCurve is to appear within a line feature
    to express the structural and geometric relationships of this
    feature to other features via the shared edge definitions. If
    provided, the aggregationType attribute shall have the value
    "sequence".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FaceOrTopoSolidPropertyType:
    face: Optional[Face] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
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
class TopoCurvePropertyType:
    topo_curve: Optional[TopoCurve] = field(
        default=None,
        metadata={
            "name": "TopoCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodeType(AbstractTopoPrimitiveType):
    """
    :ivar container:
    :ivar directed_edge: In the case of planar topology, a gml:Node must
        have a clockwise sequence of gml:directedEdge properties, to
        ensure a lossless topology representation as defined by
        Kuijpers, et. al. (see OGC 05-102 Topology IPR).
    :ivar point_property:
    :ivar aggregation_type:
    """
    container: Optional[FaceOrTopoSolidPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
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
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class TopoCurveProperty(TopoCurvePropertyType):
    """
    The gml:topoCurveProperty property element may be used in features to express
    their relationship to the referenced topology edges.
    """
    class Meta:
        name = "topoCurveProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Node(NodeType):
    """Gml:Node represents the 0-dimensional primitive.

    The optional coboundary of a node (gml:directedEdge) is a sequence
    of directed edges which are incident on this node. Edges emanating
    from this node appear in the node coboundary with a negative
    orientation. If provided, the aggregationType attribute shall have
    the value "sequence". A node may optionally be realised by a
    0-dimensional geometric primitive (gml:pointProperty).
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class NodeOrEdgePropertyType:
    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
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
class TopoPrimitiveArrayAssociationType:
    topo_solid: List[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    face: List[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        }
    )
    node: List[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
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
class TopoPrimitiveMemberType:
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    face: Optional[Face] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
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
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    """
    The gml:topoPrimitiveMember property element encodes for the relationship
    between a topology complex and a single topology primitive.
    """
    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPrimitiveMembers(TopoPrimitiveArrayAssociationType):
    """
    The gml:topoPrimitiveMembers property element encodes the relationship between
    a topology complex and an arbitrary number of topology primitives.
    """
    class Meta:
        name = "topoPrimitiveMembers"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexType(AbstractTopologyType):
    maximal_complex: Optional[MaximalComplex] = field(
        default=None,
        metadata={
            "name": "maximalComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    super_complex: List[SuperComplex] = field(
        default_factory=list,
        metadata={
            "name": "superComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    sub_complex: List[SubComplex] = field(
        default_factory=list,
        metadata={
            "name": "subComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    topo_primitive_member: List[TopoPrimitiveMember] = field(
        default_factory=list,
        metadata={
            "name": "topoPrimitiveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    topo_primitive_members: Optional[TopoPrimitiveMembers] = field(
        default=None,
        metadata={
            "name": "topoPrimitiveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    is_maximal: bool = field(
        default=False,
        metadata={
            "name": "isMaximal",
            "type": "Attribute",
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
class TopoComplex(TopoComplexType):
    """Gml:TopoComplex is a collection of topological primitives.

    Each complex holds a reference to its maximal complex
    (gml:maximalComplex) and optionally to sub- or super-complexes
    (gml:subComplex, gml:superComplex). A topology complex contains its
    primitive and sub-complex members.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
