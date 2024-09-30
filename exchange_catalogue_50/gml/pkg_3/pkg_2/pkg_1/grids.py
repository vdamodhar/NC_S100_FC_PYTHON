from dataclasses import dataclass, field
from typing import List, Optional
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import (
    AbstractGeometryType,
    PointPropertyType,
    VectorType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridEnvelopeType:
    low: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
            "tokens": True,
        }
    )
    high: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class GridLimitsType:
    grid_envelope: Optional[GridEnvelopeType] = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class GridType(AbstractGeometryType):
    limits: Optional[GridLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        }
    )
    axis_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Grid(GridType):
    """The gml:Grid implicitly defines an unrectified grid, which is a network
    composed of two or more sets of curves in which the members of each set
    intersect the members of the other sets in an algorithmic way.

    The region of interest within the grid is given in terms of its
    gml:limits, being the grid coordinates of  diagonally opposed
    corners of a rectangular region.  gml:axisLabels is provided with a
    list of labels of the axes of the grid (gml:axisName has been
    deprecated). gml:dimension specifies the dimension of the grid. The
    gml:limits element contains a single gml:GridEnvelope. The gml:low
    and gml:high property elements of the envelope are each
    integerLists, which are coordinate tuples, the coordinates being
    measured as offsets from the origin of the grid along each axis, of
    the diagonally opposing corners of a "rectangular" region of
    interest.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RectifiedGridType(GridType):
    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    offset_vector: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )


@dataclass
class RectifiedGrid(RectifiedGridType):
    """A rectified grid is a grid for which there is an affine transformation
    between the grid coordinates and the coordinates of an external coordinate
    reference system.

    It is defined by specifying the position (in some geometric space)
    of the grid "origin" and of the vectors that specify the post
    locations. Note that the grid limits (post indexes) and axis name
    properties are inherited from gml:GridType and that
    gml:RectifiedGrid adds a gml:origin property (contains or references
    a gml:Point) and a set of gml:offsetVector properties.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
