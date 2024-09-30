from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime
from exchange_catalogue_52.s100.pkg_5.pkg_2.pkg_0.s100_se.pkg_20240415.part15 import (
    S100SeCertificateContainerType,
    S100SeDigitalSignature,
    S100SeDigitalSignatureReferencePropertyType,
    S100SeSignatureOnData,
    S100SeSignatureOnSignature,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.cit.pkg_2.pkg_0.citation import (
    CiAddressType,
    CiResponsibilityPropertyType,
    CiTelephoneType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    CharacterStringPropertyType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gex.pkg_1.pkg_0.extent import (
    ExBoundingPolygonType,
    ExGeographicBoundingBoxType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.lan.pkg_1.pkg_0.language import PtLocalePropertyType
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mco.pkg_1.pkg_0.constraints import MdClassificationCodePropertyType
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mmi.pkg_1.pkg_0.maintenance import MdMaintenanceInformationPropertyType
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mri.pkg_1.pkg_0.identification import MdUsagePropertyType

__NAMESPACE__ = "http://www.iho.int/s100/xc/5.2"


class S100CatalogueScope(Enum):
    """
    The scope of the catalogue.

    :cvar FEATURE_CATALOGUE: S-100 feature catalogue
    :cvar PORTRAYAL_CATALOGUE: S-100 portrayal catalogue
    :cvar INTEROPERABILITY_CATALOGUE: S-100 interoperability information
    """
    FEATURE_CATALOGUE = "featureCatalogue"
    PORTRAYAL_CATALOGUE = "portrayalCatalogue"
    INTEROPERABILITY_CATALOGUE = "interoperabilityCatalogue"


class S100CompliancyCategory(Enum):
    """
    :cvar CATEGORY1: IHO S-100 object model compliant
    :cvar CATEGORY2: IHO S-100 compliant with non-standard encoding
    :cvar CATEGORY3: IHO S-100 compliant with standard encoding
    :cvar CATEGORY4: IHO S-100 and IMO harmonized display compliant
    """
    CATEGORY1 = "category1"
    CATEGORY2 = "category2"
    CATEGORY3 = "category3"
    CATEGORY4 = "category4"


class S100EncodingFormat(Enum):
    """
    The encoding format.

    :cvar ISO_IEC_8211: The ISO 8211 data format as defined in Part 10a
    :cvar GML: The GML data format as defined in Part 10b
    :cvar HDF5: The HDF5 data format as defined in Part 10c
    :cvar UNDEFINED: The encoding is defined in the Product
        Specification
    """
    ISO_IEC_8211 = "ISO/IEC 8211"
    GML = "GML"
    HDF5 = "HDF5"
    UNDEFINED = "undefined"


@dataclass
class S100ExchangeCatalogueIdentifier:
    """
    An exchange catalogue contains the discovery metadata about the exchange
    datasets and support files.

    :ivar identifier: An identifier for an Exchange Catalogue.
    :ivar date_time: Creation date and time of the exchange catalogue
    """
    class Meta:
        name = "S100_ExchangeCatalogueIdentifier"
        namespace = "http://www.iho.int/s100/xc/5.2"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "required": True,
        }
    )


class S100NavigationPurpose(Enum):
    """
    The navigational purpose of the dataset.

    :cvar PORT: For port and near shore operations
    :cvar TRANSIT: For coast and planning purposes
    :cvar OVERVIEW: For ocean crossing and planning purposes
    """
    PORT = "port"
    TRANSIT = "transit"
    OVERVIEW = "overview"


class S100ProtectionScheme(Enum):
    """
    Data protection schemes.

    :cvar S100P15: IHO S-100 Part 15
    """
    S100P15 = "S100p15"


class S100Purpose(Enum):
    """
    The purpose of the dataset.

    :cvar NEW_DATASET: Brand new dataset
    :cvar NEW_EDITION: New edition of the dataset or Catalogue
    :cvar UPDATE: Dataset update
    :cvar REISSUE: Dataset that has been re-issued
    :cvar CANCELLATION: Dataset or Catalogue that has been cancelled
    :cvar DELTA: Dataset difference
    """
    NEW_DATASET = "newDataset"
    NEW_EDITION = "newEdition"
    UPDATE = "update"
    REISSUE = "reissue"
    CANCELLATION = "cancellation"
    DELTA = "delta"


class S100ResourcePurpose(Enum):
    """
    Defines the purpose of the supporting resource.

    :cvar SUPPORT_FILE: A support file
    :cvar ISOMETADATA: Dataset metadata in ISO format
    :cvar LANGUAGE_PACK: A Language pack
    :cvar GMLSCHEMA: GML Application Schema
    :cvar OTHER: A type of resource not otherwise described
    """
    SUPPORT_FILE = "supportFile"
    ISOMETADATA = "ISOMetadata"
    LANGUAGE_PACK = "languagePack"
    GMLSCHEMA = "GMLSchema"
    OTHER = "other"


class S100SupportFileFormat(Enum):
    """
    The format used for the support file.

    :cvar TXT_UTF_8: UTF-8 text excluding control codes
    :cvar JPEG2000: JPEG2000 format
    :cvar HTML: Hypertext Markup Language
    :cvar XML: Extensible Markup Language
    :cvar XSLT: Extensible Stylesheet Language Transformations
    :cvar VIDEO: Representation of moving images in unspecified format
    :cvar TIFF: Tagged Image File Format
    :cvar PDF_AOR_UA: Portable Document Format
    :cvar LUA: Lua programming language
    :cvar OTHER: Other format
    """
    TXT_UTF_8 = "TXT_UTF-8"
    JPEG2000 = "JPEG2000"
    HTML = "HTML"
    XML = "XML"
    XSLT = "XSLT"
    VIDEO = "VIDEO"
    TIFF = "TIFF"
    PDF_AOR_UA = "PDF/AorUA"
    LUA = "LUA"
    OTHER = "other"


class S100SupportFileRevisionStatus(Enum):
    """
    The reason for inclusion of the support file in this Exchange Set.

    :cvar NEW: A file which is new
    :cvar REPLACEMENT: A file which replaces an existing file
    :cvar DELETION: Deletes an existing file
    """
    NEW = "new"
    REPLACEMENT = "replacement"
    DELETION = "deletion"


@dataclass
class S100SupportFileSpecification:
    """
    The Support File Specification contains the information needed to build the
    specified product.

    :ivar name: The name of the specification used to create the support
        file.
    :ivar version: The version number of the specification.
    :ivar date: The version date of the specification.
    """
    class Meta:
        name = "S100_SupportFileSpecification"
        namespace = "http://www.iho.int/s100/xc/5.2"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class S100TemporalExtent:
    """
    Temporal extent.

    :ivar time_instant_begin: The instant at which the temporal extent
        begins
    :ivar time_instant_end: The instant at which the temporal extent
        ends
    """
    class Meta:
        name = "S100_TemporalExtent"

    time_instant_begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeInstantBegin",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/xc/5.2",
        }
    )
    time_instant_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeInstantEnd",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/xc/5.2",
        }
    )


@dataclass
class S100AddressType(CiAddressType):
    """
    Address type, derived from CI_Address.
    """
    class Meta:
        name = "S100_Address_Type"

    iso_type: str = field(
        default="cit:CI_Address",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100BoundingPolygonType(ExBoundingPolygonType):
    """
    Bounding polygon type, derived from EX_BoundingPolygon.
    """
    class Meta:
        name = "S100_BoundingPolygon_Type"

    iso_type: str = field(
        default="gex:EX_BoundingPolygon",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100ClassificationCodePropertyType(MdClassificationCodePropertyType):
    """
    Classification code derivation from ISO 19115.
    """
    class Meta:
        name = "S100_ClassificationCode_PropertyType"

    iso_type: str = field(
        default="mco:MD_ClassificationCode_Property",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100EncodingFormatPropertyType:
    """
    Property type for S100_DataFormat.
    """
    class Meta:
        name = "S100_EncodingFormat_PropertyType"

    value: Optional[S100EncodingFormat] = field(
        default=None,
        metadata={
            "required": True,
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
class S100GeographicBoundingBoxType(ExGeographicBoundingBoxType):
    """
    Geographic bounding box type, derived from EX_GeographicBoundingBox.
    """
    class Meta:
        name = "S100_GeographicBoundingBox_Type"

    iso_type: str = field(
        default="gex:EX_GeographicBoundingBox",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100PhoneType(CiTelephoneType):
    """
    Phone type, derived from CI_Telephone.
    """
    class Meta:
        name = "S100_Phone_Type"

    iso_type: str = field(
        default="cit:CI_Telephone",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100ProductSpecification:
    """
    The Product Specification contains the information needed to build the
    specified product.

    :ivar name: The name of the product specification used to create the
        datasets.
    :ivar version: The version number of the product specification.
    :ivar date: The version date of the product specification.
    :ivar product_identifier: Machine readable unique identifier of a
        product type. For example, “S-101”
    :ivar number: The number used to lookup the product in the Product
        Specification Register of the IHO GI registry
    :ivar compliancy_category: The level of compliance of the Product
        Specification to S-100
    """
    class Meta:
        name = "S100_ProductSpecification"
        namespace = "http://www.iho.int/s100/xc/5.2"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    product_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "productIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    compliancy_category: Optional[S100CompliancyCategory] = field(
        default=None,
        metadata={
            "name": "compliancyCategory",
            "type": "Element",
        }
    )


@dataclass
class S100SupportFileDiscoveryMetadata:
    """
    Metadata about the individual support files in the exchange catalogue.

    :ivar file_name: Name for the support file
    :ivar revision_status: The purpose for which the support file has
        been issued
    :ivar edition_number: The edition number of the support file
    :ivar issue_date: Date on which the data was made available by the
        data producer.
    :ivar support_file_specification: The specification used to create
        this file
    :ivar data_type: The format of the support file
    :ivar other_data_type_description: Encoding format other than those
        listed
    :ivar comment: Optional comment
    :ivar compression_flag: Indicates if the resource is compressed
    :ivar digital_signature_reference: Specifies the algorithm used to
        compute digitalSignatureValue
    :ivar digital_signature_value: Value derived from the digital
        signature. The value resulting from application of
        digitalSignatureReference. Implemented as the digital signature
        format specified in Part 15.
    :ivar default_locale: Default language and character set used in the
        support file
    :ivar supported_resource: Identifier of the resource supported by
        this support file
    :ivar resource_purpose: The purpose of the supporting resource
    """
    class Meta:
        name = "S100_SupportFileDiscoveryMetadata"
        namespace = "http://www.iho.int/s100/xc/5.2"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "required": True,
        }
    )
    revision_status: Optional[S100SupportFileRevisionStatus] = field(
        default=None,
        metadata={
            "name": "revisionStatus",
            "type": "Element",
            "required": True,
        }
    )
    edition_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "editionNumber",
            "type": "Element",
            "required": True,
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
        }
    )
    support_file_specification: Optional[S100SupportFileSpecification] = field(
        default=None,
        metadata={
            "name": "supportFileSpecification",
            "type": "Element",
        }
    )
    data_type: Optional[S100SupportFileFormat] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Element",
            "required": True,
        }
    )
    other_data_type_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherDataTypeDescription",
            "type": "Element",
        }
    )
    comment: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    compression_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "compressionFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    digital_signature_reference: Optional[S100SeDigitalSignatureReferencePropertyType] = field(
        default=None,
        metadata={
            "name": "digitalSignatureReference",
            "type": "Element",
            "required": True,
        }
    )
    digital_signature_value: List["S100SupportFileDiscoveryMetadata.DigitalSignatureValue"] = field(
        default_factory=list,
        metadata={
            "name": "digitalSignatureValue",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    default_locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "name": "defaultLocale",
            "type": "Element",
        }
    )
    supported_resource: List[str] = field(
        default_factory=list,
        metadata={
            "name": "supportedResource",
            "type": "Element",
        }
    )
    resource_purpose: Optional[S100ResourcePurpose] = field(
        default=None,
        metadata={
            "name": "resourcePurpose",
            "type": "Element",
        }
    )

    @dataclass
    class DigitalSignatureValue:
        s100_se_signature_on_data: Optional[S100SeSignatureOnData] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnData",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_signature_on_signature: Optional[S100SeSignatureOnSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_digital_signature: Optional[S100SeDigitalSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_DigitalSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )


@dataclass
class S100UsagePropertyType(MdUsagePropertyType):
    """
    Restriction code derivation from ISO 19115.
    """
    class Meta:
        name = "S100_Usage_PropertyType"

    iso_type: str = field(
        default="mri:MD_Usage_Property",
        metadata={
            "name": "isoType",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )


@dataclass
class S100CatalogueDiscoveryMetadata:
    """
    Substitution group head element.

    :ivar file_name: The name for the catalogue
    :ivar purpose: The purpose for which the Catalogue has been issued
    :ivar edition_number: The Edition number of the Catalogue
    :ivar scope: Subject domain of the catalogue.
    :ivar version_number: The version identifier of the Catalogue
    :ivar issue_date: The issue date of the Catalogue
    :ivar product_specification: The product specification used to
        create this file.
    :ivar digital_signature_reference: Specifies the algorithm used to
        compute digitalSignatureValue
    :ivar digital_signature_value: Value derived from the digital
        signature. The value resulting from application of
        digitalSignatureReference. Implemented as the digital signature
        format specified in Part 15.
    :ivar compression_flag: Indicates if the resource is compressed
    :ivar default_locale: Default language and character set used in the
        Catalogue
    :ivar other_locale: Other languages and character sets used in the
        Catalogue
    """
    class Meta:
        name = "S100_CatalogueDiscoveryMetadata"
        namespace = "http://www.iho.int/s100/xc/5.2"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "required": True,
        }
    )
    purpose: Optional[S100Purpose] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    edition_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "editionNumber",
            "type": "Element",
            "required": True,
        }
    )
    scope: Optional[S100CatalogueScope] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    version_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionNumber",
            "type": "Element",
            "required": True,
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "required": True,
        }
    )
    product_specification: Optional[S100ProductSpecification] = field(
        default=None,
        metadata={
            "name": "productSpecification",
            "type": "Element",
            "required": True,
        }
    )
    digital_signature_reference: Optional[S100SeDigitalSignatureReferencePropertyType] = field(
        default=None,
        metadata={
            "name": "digitalSignatureReference",
            "type": "Element",
            "required": True,
        }
    )
    digital_signature_value: List["S100CatalogueDiscoveryMetadata.DigitalSignatureValue"] = field(
        default_factory=list,
        metadata={
            "name": "digitalSignatureValue",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    compression_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "compressionFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    default_locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "name": "defaultLocale",
            "type": "Element",
        }
    )
    other_locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherLocale",
            "type": "Element",
        }
    )

    @dataclass
    class DigitalSignatureValue:
        s100_se_signature_on_data: Optional[S100SeSignatureOnData] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnData",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_signature_on_signature: Optional[S100SeSignatureOnSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_digital_signature: Optional[S100SeDigitalSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_DigitalSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )


@dataclass
class S100CataloguePointofContact:
    """
    Contact details of the issuer of this exchange catalogue.

    :ivar organization: The organization distributing this exchange
        catalogue. This could be an individual producer, value added
        reseller, etc.
    :ivar phone:
    :ivar address:
    """
    class Meta:
        name = "S100_CataloguePointofContact"

    organization: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/xc/5.2",
            "required": True,
        }
    )
    phone: Optional[S100PhoneType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/xc/5.2",
        }
    )
    address: Optional[S100AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/xc/5.2",
        }
    )


@dataclass
class S100DataCoverage:
    """
    Definition required.

    :ivar bounding_polygon: A polygon which defines the actual data
        limit.
    :ivar temporal_extent: Specification of the temporal extent of the
        coverage
    :ivar optimum_display_scale: The scale with which the data is
        optimally displayed
    :ivar maximum_display_scale: The maximum scale with which the data
        is displayed
    :ivar minimum_display_scale: The minimum scale with which the data
        is displayed
    :ivar approximate_grid_resolution: The resolution of gridded or
        georeferenced data (in metres)
    """
    class Meta:
        name = "S100_DataCoverage"
        namespace = "http://www.iho.int/s100/xc/5.2"

    bounding_polygon: Optional[S100BoundingPolygonType] = field(
        default=None,
        metadata={
            "name": "boundingPolygon",
            "type": "Element",
            "required": True,
        }
    )
    temporal_extent: Optional[S100TemporalExtent] = field(
        default=None,
        metadata={
            "name": "temporalExtent",
            "type": "Element",
        }
    )
    optimum_display_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "optimumDisplayScale",
            "type": "Element",
        }
    )
    maximum_display_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumDisplayScale",
            "type": "Element",
        }
    )
    minimum_display_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumDisplayScale",
            "type": "Element",
        }
    )
    approximate_grid_resolution: List[float] = field(
        default_factory=list,
        metadata={
            "name": "approximateGridResolution",
            "type": "Element",
        }
    )


@dataclass
class S100DatasetDiscoveryMetadata:
    """
    Metadata about the individual datasets in the exchange catalogue.

    :ivar file_name: Dataset file name
    :ivar description: Short description giving the area or location
        covered by the dataset. e.g. a harbour or port name, between two
        named locations etc.
    :ivar dataset_id: Dataset ID expressed as a Marine Resource Name
    :ivar compression_flag: Indicates if the resource is compressed
    :ivar data_protection: Indicates if the data is encrypted
    :ivar protection_scheme: Specification of method used for data
        protection
    :ivar digital_signature_reference: Digital Signature of the file.
        Specifies the algorithm used to compute digitalSignatureValue
    :ivar digital_signature_value: Value derived from the digital
        signature. The value resulting from application of
        digitalSignatureReference. Implemented as the digital signature
        format specified in Part 15.
    :ivar copyright: Indicates if the dataset is copyrighted
    :ivar classification: Indicates the security classification of the
        dataset
    :ivar purpose: The purpose for which the dataset has been issued.
    :ivar not_for_navigation: Indicates the dataset is not intended to
        be used for navigation
    :ivar specific_usage: The use for which the dataset is intended.
        e.g. in the case of ENCs this would be a navigation purpose
        classification.
    :ivar edition_number: The edition number of the dataset. When a data
        set is initially created, the edition number 1 is assigned to
        it. The edition number is increased by 1 at each new edition.
        Edition number remains the same for a re-issue.
    :ivar update_number: Update number assigned to the dataset and
        increased by one for each subsequent update. Update number 0 is
        assigned to a new dataset.
    :ivar update_application_date: This date is only used for the base
        cell files (i.e. new data sets, re-issue and new edition), not
        update cell files. All updates dated on or before this date must
        have been applied by the producer.
    :ivar reference_id: Reference back to the datasetID
    :ivar issue_date: Date on which the data was made available by the
        data producer.
    :ivar issue_time: Time of day at which the data was made available
        by the data producer.
    :ivar bounding_box: The extent of the dataset limits.
    :ivar temporal_extent: Specification of the temporal extent of the
        dataset
    :ivar product_specification: The product specification used to
        create this dataset.
    :ivar producing_agency: ProducingAgency
    :ivar producer_code: The official IHO Producer Code from S-62
    :ivar encoding_format: The encoding format of the dataset.
    :ivar data_coverage: Provides information about data coverages
        within the dataset.
    :ivar comment: Any additional information
    :ivar default_locale: Default language and character set used in the
        dataset
    :ivar other_locale: Other languages and character sets used in the
        dataset
    :ivar metadata_point_of_contact: Point of contact for metadata
    :ivar metadata_date_stamp: Date stamp for metadata
    :ivar replaced_data: Indicates if a cancelled data file is cancelled
        is replaced by another data file
    :ivar data_replacement: Dataset name
    :ivar navigation_purpose: Classification of intended navigation
        purpose (for Catalogue indexing purposes)
    :ivar resource_maintenance: S-100 restricts the ISO 19115-class to:
        (i) prohibit maintenanceScope, maintenanceNote, and contact
        attributes; (ii) define restrictions on
        maintenanceAndUpdateFrequency, maintenanceDate, and
        userDefinedMaintenanceFrequency attributes
    """
    class Meta:
        name = "S100_DatasetDiscoveryMetadata"
        namespace = "http://www.iho.int/s100/xc/5.2"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "required": True,
        }
    )
    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dataset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetID",
            "type": "Element",
            "pattern": r"urn:mrn:.+",
        }
    )
    compression_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "compressionFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    data_protection: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataProtection",
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    protection_scheme: Optional[S100ProtectionScheme] = field(
        default=None,
        metadata={
            "name": "protectionScheme",
            "type": "Element",
        }
    )
    digital_signature_reference: Optional[S100SeDigitalSignatureReferencePropertyType] = field(
        default=None,
        metadata={
            "name": "digitalSignatureReference",
            "type": "Element",
            "required": True,
        }
    )
    digital_signature_value: List["S100DatasetDiscoveryMetadata.DigitalSignatureValue"] = field(
        default_factory=list,
        metadata={
            "name": "digitalSignatureValue",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    copyright: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    classification: Optional[S100ClassificationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    purpose: Optional[S100Purpose] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    not_for_navigation: Optional[str] = field(
        default=None,
        metadata={
            "name": "notForNavigation",
            "type": "Element",
            "required": True,
            "pattern": r"(true)|(false)",
        }
    )
    specific_usage: Optional[S100UsagePropertyType] = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
        }
    )
    edition_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "editionNumber",
            "type": "Element",
        }
    )
    update_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "updateNumber",
            "type": "Element",
        }
    )
    update_application_date: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "name": "updateApplicationDate",
            "type": "Element",
        }
    )
    reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceID",
            "type": "Element",
            "pattern": r"urn:mrn:.+",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "required": True,
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "issueTime",
            "type": "Element",
        }
    )
    bounding_box: Optional[S100GeographicBoundingBoxType] = field(
        default=None,
        metadata={
            "name": "boundingBox",
            "type": "Element",
        }
    )
    temporal_extent: Optional[S100TemporalExtent] = field(
        default=None,
        metadata={
            "name": "temporalExtent",
            "type": "Element",
        }
    )
    product_specification: Optional[S100ProductSpecification] = field(
        default=None,
        metadata={
            "name": "productSpecification",
            "type": "Element",
            "required": True,
        }
    )
    producing_agency: Optional[CiResponsibilityPropertyType] = field(
        default=None,
        metadata={
            "name": "producingAgency",
            "type": "Element",
            "required": True,
        }
    )
    producer_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "producerCode",
            "type": "Element",
        }
    )
    encoding_format: Optional[S100EncodingFormatPropertyType] = field(
        default=None,
        metadata={
            "name": "encodingFormat",
            "type": "Element",
            "required": True,
        }
    )
    data_coverage: List[S100DataCoverage] = field(
        default_factory=list,
        metadata={
            "name": "dataCoverage",
            "type": "Element",
        }
    )
    comment: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    default_locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "name": "defaultLocale",
            "type": "Element",
        }
    )
    other_locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherLocale",
            "type": "Element",
        }
    )
    metadata_point_of_contact: Optional[CiResponsibilityPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataPointOfContact",
            "type": "Element",
        }
    )
    metadata_date_stamp: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "metadataDateStamp",
            "type": "Element",
        }
    )
    replaced_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "replacedData",
            "type": "Element",
            "pattern": r"(true)|(false)",
        }
    )
    data_replacement: List[str] = field(
        default_factory=list,
        metadata={
            "name": "dataReplacement",
            "type": "Element",
        }
    )
    navigation_purpose: List[S100NavigationPurpose] = field(
        default_factory=list,
        metadata={
            "name": "navigationPurpose",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    resource_maintenance: Optional[MdMaintenanceInformationPropertyType] = field(
        default=None,
        metadata={
            "name": "resourceMaintenance",
            "type": "Element",
        }
    )

    @dataclass
    class DigitalSignatureValue:
        s100_se_signature_on_data: Optional[S100SeSignatureOnData] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnData",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_signature_on_signature: Optional[S100SeSignatureOnSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_SignatureOnSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )
        s100_se_digital_signature: Optional[S100SeDigitalSignature] = field(
            default=None,
            metadata={
                "name": "S100_SE_DigitalSignature",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
            }
        )


@dataclass
class S100ExchangeCatalogue:
    """
    Each exchange set has a single S-100_ExchangeCatalogue which contains meta
    information for the data and support files in the exchange set.

    :ivar identifier: Uniquely identifies this exchange catalogue
    :ivar contact: Details about the issuer of this exchange catalogue
    :ivar product_specification: Details about the product
        specifications used for the datasets contained in the exchange
        catalogue. Conditional on all the datasets using the same
        product specification.
    :ivar default_locale: Default language and character set used for
        all metadata records in this Exchange Catalogue
    :ivar other_locale: Other languages and character sets used for the
        localized metadata records in this Exchange Catalogue
    :ivar exchange_catalogue_description: Description of what the
        exchange catalogue contains
    :ivar exchange_catalogue_comment: Any additional Information
    :ivar certificates: Signed public key certificates referred to by
        digital signatures in the Exchange Set
    :ivar data_server_identifier: Identifies the data server for the
        permit
    :ivar dataset_discovery_metadata: Container for
        S100_DatasetDiscoveryMetadata elements
    :ivar support_file_discovery_metadata: Exchange Catalogues may
        include or reference discovery metadata for the support files in
        the Exchange Set
    :ivar catalogue_discovery_metadata: Metadata for Catalogue
    """
    class Meta:
        name = "S100_ExchangeCatalogue"
        namespace = "http://www.iho.int/s100/xc/5.2"

    identifier: Optional[S100ExchangeCatalogueIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contact: Optional[S100CataloguePointofContact] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    product_specification: List[S100ProductSpecification] = field(
        default_factory=list,
        metadata={
            "name": "productSpecification",
            "type": "Element",
        }
    )
    default_locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "name": "defaultLocale",
            "type": "Element",
        }
    )
    other_locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherLocale",
            "type": "Element",
        }
    )
    exchange_catalogue_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "exchangeCatalogueDescription",
            "type": "Element",
        }
    )
    exchange_catalogue_comment: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "exchangeCatalogueComment",
            "type": "Element",
        }
    )
    certificates: List[S100SeCertificateContainerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    data_server_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataServerIdentifier",
            "type": "Element",
        }
    )
    dataset_discovery_metadata: Optional["S100ExchangeCatalogue.DatasetDiscoveryMetadata"] = field(
        default=None,
        metadata={
            "name": "datasetDiscoveryMetadata",
            "type": "Element",
            "required": True,
        }
    )
    support_file_discovery_metadata: Optional["S100ExchangeCatalogue.SupportFileDiscoveryMetadata"] = field(
        default=None,
        metadata={
            "name": "supportFileDiscoveryMetadata",
            "type": "Element",
            "required": True,
        }
    )
    catalogue_discovery_metadata: Optional["S100ExchangeCatalogue.CatalogueDiscoveryMetadata"] = field(
        default=None,
        metadata={
            "name": "catalogueDiscoveryMetadata",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class DatasetDiscoveryMetadata:
        """
        :ivar s100_dataset_discovery_metadata: Discovery metadata for
            single dataset. Constraints should be in a separate file for
            reusability and potential customization.
        """
        s100_dataset_discovery_metadata: List[S100DatasetDiscoveryMetadata] = field(
            default_factory=list,
            metadata={
                "name": "S100_DatasetDiscoveryMetadata",
                "type": "Element",
            }
        )

    @dataclass
    class SupportFileDiscoveryMetadata:
        s100_support_file_discovery_metadata: List[S100SupportFileDiscoveryMetadata] = field(
            default_factory=list,
            metadata={
                "name": "S100_SupportFileDiscoveryMetadata",
                "type": "Element",
            }
        )

    @dataclass
    class CatalogueDiscoveryMetadata:
        s100_catalogue_discovery_metadata: List[S100CatalogueDiscoveryMetadata] = field(
            default_factory=list,
            metadata={
                "name": "S100_CatalogueDiscoveryMetadata",
                "type": "Element",
            }
        )
