from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    BooleanPropertyType,
    CharacterStringPropertyType,
    GenericNamePropertyType,
    IntegerPropertyType,
    MemberNamePropertyType,
    RealPropertyType,
    RecordTypePropertyType,
    UomLengthPropertyType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gmd.citation import CiCitationPropertyType
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gmd.reference_system import MdIdentifierPropertyType
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdContentInformationType(AbstractObjectType):
    class Meta:
        name = "AbstractMD_ContentInformation_Type"


@dataclass
class MdCoverageContentTypeCode(CodeListValueType):
    class Meta:
        name = "MD_CoverageContentTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImagingConditionCode(CodeListValueType):
    class Meta:
        name = "MD_ImagingConditionCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRangeDimensionType(AbstractObjectType):
    """
    Set of adjacent wavelengths in the electro-magnetic spectrum with a common
    characteristic, such as the visible band.
    """
    class Meta:
        name = "MD_RangeDimension_Type"

    sequence_identifier: Optional[MemberNamePropertyType] = field(
        default=None,
        metadata={
            "name": "sequenceIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    descriptor: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdBandType(MdRangeDimensionType):
    class Meta:
        name = "MD_Band_Type"

    max_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    min_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    units: Optional[UomLengthPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    peak_response: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "peakResponse",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    bits_per_value: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "bitsPerValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    tone_gradation: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "toneGradation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    scale_factor: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    offset: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdCoverageContentTypeCodePropertyType:
    class Meta:
        name = "MD_CoverageContentTypeCode_PropertyType"

    md_coverage_content_type_code: Optional[MdCoverageContentTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_CoverageContentTypeCode",
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
class MdFeatureCatalogueDescriptionType(AbstractMdContentInformationType):
    """
    Information identifing the feature catalogue.
    """
    class Meta:
        name = "MD_FeatureCatalogueDescription_Type"

    compliance_code: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "complianceCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    language: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    included_with_dataset: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "includedWithDataset",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    feature_types: List[GenericNamePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureTypes",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    feature_catalogue_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class MdImagingConditionCodePropertyType:
    class Meta:
        name = "MD_ImagingConditionCode_PropertyType"

    md_imaging_condition_code: Optional[MdImagingConditionCode] = field(
        default=None,
        metadata={
            "name": "MD_ImagingConditionCode",
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
class MdRangeDimension(MdRangeDimensionType):
    class Meta:
        name = "MD_RangeDimension"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBand(MdBandType):
    class Meta:
        name = "MD_Band"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFeatureCatalogueDescription(MdFeatureCatalogueDescriptionType):
    class Meta:
        name = "MD_FeatureCatalogueDescription"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBandPropertyType:
    class Meta:
        name = "MD_Band_PropertyType"

    md_band: Optional[MdBand] = field(
        default=None,
        metadata={
            "name": "MD_Band",
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
class MdFeatureCatalogueDescriptionPropertyType:
    class Meta:
        name = "MD_FeatureCatalogueDescription_PropertyType"

    md_feature_catalogue_description: Optional[MdFeatureCatalogueDescription] = field(
        default=None,
        metadata={
            "name": "MD_FeatureCatalogueDescription",
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
class MdRangeDimensionPropertyType:
    class Meta:
        name = "MD_RangeDimension_PropertyType"

    md_band: Optional[MdBand] = field(
        default=None,
        metadata={
            "name": "MD_Band",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_range_dimension: Optional[MdRangeDimension] = field(
        default=None,
        metadata={
            "name": "MD_RangeDimension",
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
class MdCoverageDescriptionType(AbstractMdContentInformationType):
    """
    Information about the domain of the raster cell.
    """
    class Meta:
        name = "MD_CoverageDescription_Type"

    attribute_description: Optional[RecordTypePropertyType] = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    content_type: Optional[MdCoverageContentTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    dimension: List[MdRangeDimensionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdCoverageDescription(MdCoverageDescriptionType):
    class Meta:
        name = "MD_CoverageDescription"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImageDescriptionType(MdCoverageDescriptionType):
    """
    Information about an image's suitability for use.
    """
    class Meta:
        name = "MD_ImageDescription_Type"

    illumination_elevation_angle: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "illuminationElevationAngle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    illumination_azimuth_angle: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "illuminationAzimuthAngle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    imaging_condition: Optional[MdImagingConditionCodePropertyType] = field(
        default=None,
        metadata={
            "name": "imagingCondition",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    image_quality_code: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "imageQualityCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    cloud_cover_percentage: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "cloudCoverPercentage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    processing_level_code: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "processingLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    compression_generation_quantity: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "compressionGenerationQuantity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    triangulation_indicator: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "triangulationIndicator",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    radiometric_calibration_data_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "radiometricCalibrationDataAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    camera_calibration_information_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "cameraCalibrationInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    film_distortion_information_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "filmDistortionInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    lens_distortion_information_availability: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "lensDistortionInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdImageDescription(MdImageDescriptionType):
    class Meta:
        name = "MD_ImageDescription"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdContentInformationPropertyType:
    class Meta:
        name = "MD_ContentInformation_PropertyType"

    md_image_description: Optional[MdImageDescription] = field(
        default=None,
        metadata={
            "name": "MD_ImageDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_coverage_description: Optional[MdCoverageDescription] = field(
        default=None,
        metadata={
            "name": "MD_CoverageDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_feature_catalogue_description: Optional[MdFeatureCatalogueDescription] = field(
        default=None,
        metadata={
            "name": "MD_FeatureCatalogueDescription",
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
class MdCoverageDescriptionPropertyType:
    class Meta:
        name = "MD_CoverageDescription_PropertyType"

    md_image_description: Optional[MdImageDescription] = field(
        default=None,
        metadata={
            "name": "MD_ImageDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_coverage_description: Optional[MdCoverageDescription] = field(
        default=None,
        metadata={
            "name": "MD_CoverageDescription",
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
class MdImageDescriptionPropertyType:
    class Meta:
        name = "MD_ImageDescription_PropertyType"

    md_image_description: Optional[MdImageDescription] = field(
        default=None,
        metadata={
            "name": "MD_ImageDescription",
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
