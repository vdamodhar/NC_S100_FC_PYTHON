from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    CodeType,
    CoordinatesType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import (
    IncrementOrder,
    MappingRule,
    GridDomain,
    MultiCurveDomain,
    MultiPointDomain,
    MultiSolidDomain,
    MultiSurfaceDomain,
    RectifiedGridDomain,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.feature import AbstractFeatureType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_aggregates import (
    MultiCurve,
    MultiGeometry,
    MultiPoint,
    MultiSolid,
    MultiSurface,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    LineString,
    Point,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic2d import (
    LinearRing,
    Polygon,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_complexes import (
    CompositeCurve,
    CompositeSolid,
    CompositeSurface,
    GeometricComplex,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_primitives import (
    Curve,
    OrientableCurve,
    OrientableSurface,
    PolyhedralSurface,
    Ring,
    Shell,
    Solid,
    Surface,
    Tin,
    TriangulatedSurface,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import (
    AssociationRoleType,
    ReferenceType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.grids import (
    Grid,
    RectifiedGrid,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal import (
    TimeInstant,
    TimePeriod,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.temporal_topology import (
    TimeEdge,
    TimeNode,
    TimeTopologyComplex,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.value_objects import (
    CategoryList,
    QuantityList,
    ValueArray,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class SequenceRuleEnumeration(Enum):
    LINEAR = "Linear"
    BOUSTROPHEDONIC = "Boustrophedonic"
    CANTOR_DIAGONAL = "Cantor-diagonal"
    SPIRAL = "Spiral"
    MORTON = "Morton"
    HILBERT = "Hilbert"


@dataclass
class DomainSetType:
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
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_edge: Optional[TimeEdge] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
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
class MappingRuleType:
    rule_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "ruleDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    rule_reference: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ruleReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class SequenceRuleType:
    """The gml:SequenceRuleType is derived from the gml:SequenceRuleEnumeration
    through the addition of an axisOrder attribute.

    The gml:SequenceRuleEnumeration is an enumerated type. The rule
    names are defined in ISO 19123. If no rule name is specified the
    default is "Linear".
    """
    value: Optional[SequenceRuleEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[IncrementOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis_order: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisOrder",
            "type": "Attribute",
            "pattern": r"[\+\-][1-9][0-9]*",
            "tokens": True,
        }
    )


@dataclass
class DoubleOrNilReasonTupleList:
    """Gml:doubleOrNilReasonList consists of a list of gml:doubleOrNilReason
    values, each separated by a whitespace.

    The gml:doubleOrNilReason values are grouped into tuples where the
    dimension of each tuple in the list is equal to the number of range
    parameters.
    """
    class Meta:
        name = "doubleOrNilReasonTupleList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )


@dataclass
class RangeParameters(AssociationRoleType):
    class Meta:
        name = "rangeParameters"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TupleList(CoordinatesType):
    """Gml:CoordinatesType consists of a list of coordinate tuples, with each
    coordinate tuple separated by the ts or tuple separator (whitespace), and each
    coordinate in the tuple by the cs or coordinate separator (comma).

    The gml:tupleList encoding is effectively "band-interleaved".
    """
    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageMappingRule(MappingRuleType):
    """Gml:CoverageMappingRule provides a formal or informal description of the
    coverage function.

    The mapping rule may be defined as an in-line string
    (gml:ruleDefinition) or via a remote reference through xlink:href
    (gml:ruleReference). If no rule name is specified, the default is
    'Linear' with respect to members of the domain in document order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DataBlockType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    tuple_list: Optional[TupleList] = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    double_or_nil_reason_tuple_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "doubleOrNilReasonTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )


@dataclass
class FileType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    file_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    file_structure: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    compression: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class GridFunctionType:
    sequence_rule: Optional[SequenceRuleType] = field(
        default=None,
        metadata={
            "name": "sequenceRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    start_point: List[int] = field(
        default_factory=list,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        }
    )


@dataclass
class DomainSet(DomainSetType):
    """The gml:domainSet property element describes the spatio-temporal region of
    interest, within which the coverage is defined.

    Its content model is given by gml:DomainSetType. The value of the
    domain is thus a choice between a gml:AbstractGeometry and a
    gml:AbstractTimeObject.  In the instance these abstract elements
    will normally be substituted by a geometry complex or temporal
    complex, to represent spatial coverages and time-series,
    respectively. The presence of the gml:AssociationAttributeGroup
    means that domainSet follows the usual GML property model and may
    use the xlink:href attribute to point to the domain, as an
    alternative to describing the domain inline. Ownership semantics may
    be provided using the gml:OwnershipAttributeGroup.
    """
    class Meta:
        name = "domainSet"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DataBlock(DataBlockType):
    """Gml:DataBlock describes the Range as a block of text encoded values similar
    to a Common Separated Value (CSV) representation.

    The range set parameterization is described by the property
    gml:rangeParameters.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class File(FileType):
    """For efficiency reasons, GML also provides a means of encoding the range set
    in an arbitrary external encoding, such as a binary file.

    This encoding may be "well-known" but this is not required. This
    mode uses the gml:File element. The values of the coverage
    (attribute values in the range set) are transmitted in a external
    file that is referenced from the XML structure described by
    gml:FileType.  The external file is referenced by the
    gml:fileReference property that is an anyURI (the gml:fileName
    property has been deprecated).  This means that the external file
    may be located remotely from the referencing GML instance. The
    gml:compression property points to a definition of a compression
    algorithm through an anyURI.  This may be a retrievable, computable
    definition or simply a reference to an unambiguous name for the
    compression method. The gml:mimeType property points to a definition
    of the file mime type. The gml:fileStructure property is defined by
    a codelist. Note further that all values shall be enclosed in a
    single file. Multi-file structures for values are not supported in
    GML. The semantics of the range set is described as above using the
    gml:rangeParameters property. Note that if any compression algorithm
    is applied, the structure above applies only to the pre-compression
    or post-decompression structure of the file. Note that the fields
    within a record match the gml:valueComponents of the
    gml:CompositeValue in document order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GridFunction(GridFunctionType):
    """Gml:GridFunction provides an explicit mapping rule for grid geometries, i.e.
    the domain shall be a geometry of type grid.

    It describes the mapping of grid posts (discrete point grid
    coverage) or grid cells (discrete surface coverage) to the values in
    the range set. The gml:startPoint is the index position of a point
    in the grid that is mapped to the first point in the range set (this
    is also the index position of the first grid post).  If the
    gml:startPoint property is omitted the gml:startPoint is assumed to
    be equal to the value of gml:low in the gml:Grid geometry.
    Subsequent points in the mapping are determined by the value of the
    gml:sequenceRule.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageFunctionType:
    mapping_rule: Optional[MappingRule] = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coverage_mapping_rule: Optional[CoverageMappingRule] = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class RangeSetType:
    value_array: List[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
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
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class CoverageFunction(CoverageFunctionType):
    """The gml:coverageFunction property describes the mapping function from the
    domain to the range of the coverage.

    The value of the CoverageFunction is one of gml:CoverageMappingRule
    and gml:GridFunction. If the gml:coverageFunction property is
    omitted for a gridded coverage (including rectified gridded
    coverages) the gml:startPoint is assumed to be the value of the
    gml:low property in the gml:Grid geometry, and the gml:sequenceRule
    is assumed to be linear and the gml:axisOrder property is assumed to
    be "+1 +2".
    """
    class Meta:
        name = "coverageFunction"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RangeSet(RangeSetType):
    """The gml:rangeSet property element contains the values of the coverage
    (sometimes called the attribute values).

    Its content model is given by gml:RangeSetType. This content model
    supports a structural description of the range.  The semantic
    information describing the range set is embedded using a uniform
    method, as part of the explicit values, or as a template value
    accompanying the representation using gml:DataBlock and gml:File.
    The values from each component (or "band") in the range may be
    encoded within a gml:ValueArray element or a concrete member of the
    gml:AbstractScalarValueList substitution group . Use of these
    elements satisfies the value-type homogeneity requirement.
    """
    class Meta:
        name = "rangeSet"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoverageType(AbstractFeatureType):
    """The base type for coverages is gml:AbstractCoverageType.

    The basic elements of a coverage can be seen in this content model: the coverage contains gml:domainSet and gml:rangeSet properties. The gml:domainSet property describes the domain of the coverage and the gml:rangeSet property describes the range of the coverage.
    """
    rectified_grid_domain: Optional[RectifiedGridDomain] = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    grid_domain: Optional[GridDomain] = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_solid_domain: Optional[MultiSolidDomain] = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_surface_domain: Optional[MultiSurfaceDomain] = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_curve_domain: Optional[MultiCurveDomain] = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    domain_set: Optional[DomainSet] = field(
        default=None,
        metadata={
            "name": "domainSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    range_set: Optional[RangeSet] = field(
        default=None,
        metadata={
            "name": "rangeSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class AbstractContinuousCoverageType(AbstractCoverageType):
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DiscreteCoverageType(AbstractCoverageType):
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class GridCoverage(DiscreteCoverageType):
    """A gml:GriddedCoverage is a discrete point coverage in which the domain set
    is a geometric grid of points.

    Note that this is the same as the gml:MultiPointCoverage except that
    we have a gml:Grid to describe the domain. The simple gridded
    coverage is not geometrically referenced and hence no geometric
    positions are assignable to the points in the grid. Such geometric
    positioning is introduced in the gml:RectifiedGridCoverage.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveCoverage(DiscreteCoverageType):
    """In a gml:MultiCurveCoverage the domain is partioned into a collection of
    curves comprising a gml:MultiCurve.  The coverage function then maps each curve
    in the collection to a value in the range set. The content model is identical
    with gml:DiscreteCoverageType, but that gml:domainSet shall have values
    gml:MultiCurve.

    In a gml:MultiCurveCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the curves of the gml:MultiCurve are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the curves of the gml:MultiCurve are mapped to the members of the composite value in document order.
    -       For gml:File encodings the curves of the gml:MultiCurve are mapped to the records of the file in sequential order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointCoverage(DiscreteCoverageType):
    """In a gml:MultiPointCoverage the domain set is a gml:MultiPoint, that is a
    collection of arbitrarily distributed geometric points. The content model is
    identical with gml:DiscreteCoverageType, but that gml:domainSet shall have
    values gml:MultiPoint.

    In a gml:MultiPointCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the points of the gml:MultiPoint are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the points of the gml:MultiPoint are mapped to the members of the composite value in document order.
    -       For gml:File encodings the points of the gml:MultiPoint are mapped to the records of the file in sequential order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidCoverage(DiscreteCoverageType):
    """In a gml:MultiSolidCoverage the domain is partioned into a collection of
    solids comprising a gml:MultiSolid.  The coverage function than maps each solid
    in the collection to a value in the range set. The content model is identical
    with gml:DiscreteCoverageType, but that gml:domainSet shall have values
    gml:MultiSolid.

    In a gml:MultiSolidCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the solids of the gml:MultiSolid are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the solids of the gml:MultiSolid are mapped to the members of the composite value in document order.
    -       For gml:File encodings the solids of the gml:MultiSolid are mapped to the records of the file in sequential order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfaceCoverage(DiscreteCoverageType):
    """In a gml:MultiSurfaceCoverage the domain is partioned into a collection of
    surfaces comprising a gml:MultiSurface.  The coverage function than maps each
    surface in the collection to a value in the range set. The content model is
    identical with gml:DiscreteCoverageType, but that gml:domainSet shall have
    values gml:MultiSurface.

    In a gml:MultiSurfaceCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the surfaces of the gml:MultiSurface are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the surfaces of the gml:MultiSurface are mapped to the members of the composite value in document order.
    -       For gml:File encodings the surfaces of the gml:MultiSurface are mapped to the records of the file in sequential order.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RectifiedGridCoverage(DiscreteCoverageType):
    """The gml:RectifiedGridCoverage is a discrete point coverage based on a
    rectified grid.

    It is similar to the grid coverage except that the points of the
    grid are geometrically referenced. The rectified grid coverage has a
    domain that is a gml:RectifiedGrid geometry.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
