from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    BooleanPropertyType,
    CharacterStringPropertyType,
    IntegerPropertyType,
    MeasurePropertyType,
    RecordPropertyType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gmd.citation import CiCitationPropertyType
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gss.geometry import GmPointPropertyType
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


class MdPixelOrientationCodeType(Enum):
    CENTER = "center"
    LOWER_LEFT = "lowerLeft"
    LOWER_RIGHT = "lowerRight"
    UPPER_RIGHT = "upperRight"
    UPPER_LEFT = "upperLeft"


@dataclass
class AbstractMdSpatialRepresentationType(AbstractObjectType):
    """
    Digital mechanism used to represent spatial information.
    """
    class Meta:
        name = "AbstractMD_SpatialRepresentation_Type"


@dataclass
class MdCellGeometryCode(CodeListValueType):
    class Meta:
        name = "MD_CellGeometryCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionNameTypeCode(CodeListValueType):
    class Meta:
        name = "MD_DimensionNameTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjectTypeCode(CodeListValueType):
    class Meta:
        name = "MD_GeometricObjectTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPixelOrientationCode:
    class Meta:
        name = "MD_PixelOrientationCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdPixelOrientationCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MdPixelOrientationCodePropertyType:
    class Meta:
        name = "MD_PixelOrientationCode_PropertyType"

    md_pixel_orientation_code: Optional[MdPixelOrientationCodeType] = field(
        default=None,
        metadata={
            "name": "MD_PixelOrientationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdTopologyLevelCode(CodeListValueType):
    class Meta:
        name = "MD_TopologyLevelCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCellGeometryCodePropertyType:
    class Meta:
        name = "MD_CellGeometryCode_PropertyType"

    md_cell_geometry_code: Optional[MdCellGeometryCode] = field(
        default=None,
        metadata={
            "name": "MD_CellGeometryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdDimensionNameTypeCodePropertyType:
    class Meta:
        name = "MD_DimensionNameTypeCode_PropertyType"

    md_dimension_name_type_code: Optional[MdDimensionNameTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DimensionNameTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGeometricObjectTypeCodePropertyType:
    class Meta:
        name = "MD_GeometricObjectTypeCode_PropertyType"

    md_geometric_object_type_code: Optional[MdGeometricObjectTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_GeometricObjectTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdTopologyLevelCodePropertyType:
    class Meta:
        name = "MD_TopologyLevelCode_PropertyType"

    md_topology_level_code: Optional[MdTopologyLevelCode] = field(
        default=None,
        metadata={
            "name": "MD_TopologyLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdDimensionType(AbstractObjectType):
    class Meta:
        name = "MD_Dimension_Type"

    dimension_name: Optional[MdDimensionNameTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dimensionName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    dimension_size: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "dimensionSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    resolution: Optional[MeasurePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdGeometricObjectsType(AbstractObjectType):
    class Meta:
        name = "MD_GeometricObjects_Type"

    geometric_object_type: Optional[MdGeometricObjectTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "geometricObjectType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    geometric_object_count: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "geometricObjectCount",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdDimension(MdDimensionType):
    class Meta:
        name = "MD_Dimension"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjects(MdGeometricObjectsType):
    class Meta:
        name = "MD_GeometricObjects"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionPropertyType:
    class Meta:
        name = "MD_Dimension_PropertyType"

    md_dimension: Optional[MdDimension] = field(
        default=None,
        metadata={
            "name": "MD_Dimension",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGeometricObjectsPropertyType:
    class Meta:
        name = "MD_GeometricObjects_PropertyType"

    md_geometric_objects: Optional[MdGeometricObjects] = field(
        default=None,
        metadata={
            "name": "MD_GeometricObjects",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGridSpatialRepresentationType(AbstractMdSpatialRepresentationType):
    """
    Types and numbers of raster spatial objects in the dataset.
    """
    class Meta:
        name = "MD_GridSpatialRepresentation_Type"

    number_of_dimensions: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "numberOfDimensions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    axis_dimension_properties: List[MdDimensionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "axisDimensionProperties",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    cell_geometry: Optional[MdCellGeometryCodePropertyType] = field(
        default=None,
        metadata={
            "name": "cellGeometry",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    transformation_parameter_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "transformationParameterAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )


@dataclass
class MdVectorSpatialRepresentationType(AbstractMdSpatialRepresentationType):
    """
    Information about the vector spatial objects in the dataset.
    """
    class Meta:
        name = "MD_VectorSpatialRepresentation_Type"

    topology_level: Optional[MdTopologyLevelCodePropertyType] = field(
        default=None,
        metadata={
            "name": "topologyLevel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    geometric_objects: List[MdGeometricObjectsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geometricObjects",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdGeorectifiedType(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_Georectified_Type"

    check_point_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "checkPointAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    check_point_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "checkPointDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    corner_points: List[GmPointPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "cornerPoints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    center_point: Optional[GmPointPropertyType] = field(
        default=None,
        metadata={
            "name": "centerPoint",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    point_in_pixel: Optional[MdPixelOrientationCodePropertyType] = field(
        default=None,
        metadata={
            "name": "pointInPixel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    transformation_dimension_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "transformationDimensionDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    transformation_dimension_mapping: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transformationDimensionMapping",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "max_occurs": 2,
        }
    )


@dataclass
class MdGeoreferenceableType(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_Georeferenceable_Type"

    control_point_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "controlPointAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    orientation_parameter_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "orientationParameterAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    orientation_parameter_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "orientationParameterDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    georeferenced_parameters: Optional[RecordPropertyType] = field(
        default=None,
        metadata={
            "name": "georeferencedParameters",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    parameter_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "parameterCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdGridSpatialRepresentation(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_GridSpatialRepresentation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdVectorSpatialRepresentation(MdVectorSpatialRepresentationType):
    class Meta:
        name = "MD_VectorSpatialRepresentation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeorectified(MdGeorectifiedType):
    class Meta:
        name = "MD_Georectified"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeoreferenceable(MdGeoreferenceableType):
    class Meta:
        name = "MD_Georeferenceable"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdVectorSpatialRepresentationPropertyType:
    class Meta:
        name = "MD_VectorSpatialRepresentation_PropertyType"

    md_vector_spatial_representation: Optional[MdVectorSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_VectorSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGeorectifiedPropertyType:
    class Meta:
        name = "MD_Georectified_PropertyType"

    md_georectified: Optional[MdGeorectified] = field(
        default=None,
        metadata={
            "name": "MD_Georectified",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGeoreferenceablePropertyType:
    class Meta:
        name = "MD_Georeferenceable_PropertyType"

    md_georeferenceable: Optional[MdGeoreferenceable] = field(
        default=None,
        metadata={
            "name": "MD_Georeferenceable",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdGridSpatialRepresentationPropertyType:
    class Meta:
        name = "MD_GridSpatialRepresentation_PropertyType"

    md_georectified: Optional[MdGeorectified] = field(
        default=None,
        metadata={
            "name": "MD_Georectified",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_georeferenceable: Optional[MdGeoreferenceable] = field(
        default=None,
        metadata={
            "name": "MD_Georeferenceable",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_grid_spatial_representation: Optional[MdGridSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_GridSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class MdSpatialRepresentationPropertyType:
    class Meta:
        name = "MD_SpatialRepresentation_PropertyType"

    md_vector_spatial_representation: Optional[MdVectorSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_VectorSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_georectified: Optional[MdGeorectified] = field(
        default=None,
        metadata={
            "name": "MD_Georectified",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_georeferenceable: Optional[MdGeoreferenceable] = field(
        default=None,
        metadata={
            "name": "MD_Georeferenceable",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_grid_spatial_representation: Optional[MdGridSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_GridSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
