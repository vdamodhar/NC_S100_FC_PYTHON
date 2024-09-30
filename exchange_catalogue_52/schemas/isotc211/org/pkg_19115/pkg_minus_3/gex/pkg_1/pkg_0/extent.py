from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    BooleanPropertyType,
    CharacterStringPropertyType,
    DecimalPropertyType,
    NilReasonEnumerationValue,
    RealPropertyType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gmw.pkg_1.pkg_0.gml_wrapper_types import (
    GmObjectPropertyType,
    ScCrsPropertyType,
    TmPrimitivePropertyType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractExtentType,
    AbstractReferenceSystemPropertyType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.common_classes import MdIdentifierPropertyType
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class AbstractExGeographicExtentType(AbstractObjectType):
    """
    :ivar extent_type_code: indication of whether the geographic element
        encompasses an area covered by the data or an area where data is
        not present
    """
    class Meta:
        name = "AbstractEX_GeographicExtent_Type"

    extent_type_code: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "extentTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )


@dataclass
class ExTemporalExtentType(AbstractObjectType):
    """
    :ivar extent: period for the content of the resource
    """
    class Meta:
        name = "EX_TemporalExtent_Type"

    extent: Optional[TmPrimitivePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )


@dataclass
class ExVerticalExtentType(AbstractObjectType):
    """
    :ivar minimum_value: lowest vertical extent contained in the
        resource
    :ivar maximum_value: highest vertical extent contained in the
        resource
    :ivar vertical_crsid:
    :ivar vertical_crs:
    """
    class Meta:
        name = "EX_VerticalExtent_Type"

    minimum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )
    maximum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )
    vertical_crsid: Optional[AbstractReferenceSystemPropertyType] = field(
        default=None,
        metadata={
            "name": "verticalCRSId",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    vertical_crs: Optional[ScCrsPropertyType] = field(
        default=None,
        metadata={
            "name": "verticalCRS",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )


@dataclass
class ExBoundingPolygonType(AbstractExGeographicExtentType):
    """
    :ivar polygon: sets of points defining the bounding polygon or any
        other GM_Object geometry (point, line or polygon)
    """
    class Meta:
        name = "EX_BoundingPolygon_Type"

    polygon: List[GmObjectPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class ExGeographicBoundingBoxType(AbstractExGeographicExtentType):
    """
    :ivar west_bound_longitude: western-most coordinate of the limit of
        the resource extent, expressed in longitude in decimal degrees
        (positive east)
    :ivar east_bound_longitude: eastern-most coordinate of the limit of
        the resource extent, expressed in longitude in decimal degrees
        (positive east)
    :ivar south_bound_latitude: southern-most coordinate of the limit of
        the resource extent, expressed in latitude in decimal degrees
        (positive north)
    :ivar north_bound_latitude: northern-most, coordinate of the limit
        of the resource extent expressed in latitude in decimal degrees
        (positive north)
    """
    class Meta:
        name = "EX_GeographicBoundingBox_Type"

    west_bound_longitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "westBoundLongitude",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )
    east_bound_longitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "eastBoundLongitude",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )
    south_bound_latitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "southBoundLatitude",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )
    north_bound_latitude: Optional[DecimalPropertyType] = field(
        default=None,
        metadata={
            "name": "northBoundLatitude",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )


@dataclass
class ExGeographicDescriptionType(AbstractExGeographicExtentType):
    """
    :ivar geographic_identifier: identifier used to represent a
        geographic area e.g. a geographic identifier as described in ISO
        19112
    """
    class Meta:
        name = "EX_GeographicDescription_Type"

    geographic_identifier: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "geographicIdentifier",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "required": True,
        }
    )


@dataclass
class ExTemporalExtent(ExTemporalExtentType):
    """
    Time period covered by the content of the resource.
    """
    class Meta:
        name = "EX_TemporalExtent"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExVerticalExtent(ExVerticalExtentType):
    """
    Vertical domain of resource.
    """
    class Meta:
        name = "EX_VerticalExtent"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExBoundingPolygon(ExBoundingPolygonType):
    """
    Enclosing geometric object which locates the resource, expressed as a set of
    (x,y) coordinate (s) NOTE: If a polygon is used it should be closed (last point
    replicates first point)
    """
    class Meta:
        name = "EX_BoundingPolygon"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExGeographicBoundingBox(ExGeographicBoundingBoxType):
    """geographic position of the resource NOTE: This is only an approximate reference so specifying the coordinate reference system is unnecessary and need only be provided with a precision of up to two decimal places"""
    class Meta:
        name = "EX_GeographicBoundingBox"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExGeographicDescription(ExGeographicDescriptionType):
    """
    Description of the geographic area using identifiers.
    """
    class Meta:
        name = "EX_GeographicDescription"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExVerticalExtentPropertyType:
    class Meta:
        name = "EX_VerticalExtent_PropertyType"

    ex_vertical_extent: Optional[ExVerticalExtent] = field(
        default=None,
        metadata={
            "name": "EX_VerticalExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class AbstractExGeographicExtentPropertyType:
    class Meta:
        name = "AbstractEX_GeographicExtent_PropertyType"

    ex_geographic_description: Optional[ExGeographicDescription] = field(
        default=None,
        metadata={
            "name": "EX_GeographicDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    ex_geographic_bounding_box: Optional[ExGeographicBoundingBox] = field(
        default=None,
        metadata={
            "name": "EX_GeographicBoundingBox",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    ex_bounding_polygon: Optional[ExBoundingPolygon] = field(
        default=None,
        metadata={
            "name": "EX_BoundingPolygon",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExBoundingPolygonPropertyType:
    class Meta:
        name = "EX_BoundingPolygon_PropertyType"

    ex_bounding_polygon: Optional[ExBoundingPolygon] = field(
        default=None,
        metadata={
            "name": "EX_BoundingPolygon",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExGeographicBoundingBoxPropertyType:
    class Meta:
        name = "EX_GeographicBoundingBox_PropertyType"

    ex_geographic_bounding_box: Optional[ExGeographicBoundingBox] = field(
        default=None,
        metadata={
            "name": "EX_GeographicBoundingBox",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExGeographicDescriptionPropertyType:
    class Meta:
        name = "EX_GeographicDescription_PropertyType"

    ex_geographic_description: Optional[ExGeographicDescription] = field(
        default=None,
        metadata={
            "name": "EX_GeographicDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExSpatialTemporalExtentType(ExTemporalExtentType):
    """
    :ivar vertical_extent: vertical extent component
    :ivar spatial_extent:
    """
    class Meta:
        name = "EX_SpatialTemporalExtent_Type"

    vertical_extent: Optional[ExVerticalExtentPropertyType] = field(
        default=None,
        metadata={
            "name": "verticalExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    spatial_extent: List[AbstractExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class ExSpatialTemporalExtent(ExSpatialTemporalExtentType):
    """
    Extent with respect to date/time and spatial boundaries.
    """
    class Meta:
        name = "EX_SpatialTemporalExtent"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExSpatialTemporalExtentPropertyType:
    class Meta:
        name = "EX_SpatialTemporalExtent_PropertyType"

    ex_spatial_temporal_extent: Optional[ExSpatialTemporalExtent] = field(
        default=None,
        metadata={
            "name": "EX_SpatialTemporalExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExTemporalExtentPropertyType:
    class Meta:
        name = "EX_TemporalExtent_PropertyType"

    ex_spatial_temporal_extent: Optional[ExSpatialTemporalExtent] = field(
        default=None,
        metadata={
            "name": "EX_SpatialTemporalExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    ex_temporal_extent: Optional[ExTemporalExtent] = field(
        default=None,
        metadata={
            "name": "EX_TemporalExtent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExExtentType(AbstractExtentType):
    """
    :ivar description: sets of points defining the bounding polygon or
        any other GM_Object geometry (point, line or polygon)
    :ivar geographic_element:
    :ivar temporal_element:
    :ivar vertical_element:
    """
    class Meta:
        name = "EX_Extent_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    geographic_element: List[AbstractExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geographicElement",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    temporal_element: List[ExTemporalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "temporalElement",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )
    vertical_element: List[ExVerticalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "verticalElement",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
        }
    )


@dataclass
class ExExtent(ExExtentType):
    """
    Extent of the resource.
    """
    class Meta:
        name = "EX_Extent"
        namespace = "http://standards.iso.org/iso/19115/-3/gex/1.0"


@dataclass
class ExExtentPropertyType:
    class Meta:
        name = "EX_Extent_PropertyType"

    ex_extent: Optional[ExExtent] = field(
        default=None,
        metadata={
            "name": "EX_Extent",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gex/1.0",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )
