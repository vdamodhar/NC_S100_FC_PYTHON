from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    CharacterStringPropertyType,
    DatePropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    ObjectReferencePropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.application_schema import MdApplicationSchemaInformationPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.citation import CiResponsiblePartyPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.constraints import MdConstraintsPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.content import MdContentInformationPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.data_quality import DqDataQualityPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.distribution import MdDistributionPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.free_text import PtLocalePropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.identification import (
    MdCharacterSetCodePropertyType,
    MdIdentificationPropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.maintenance import (
    MdMaintenanceInformationPropertyType,
    MdScopeCodePropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.metadata_application import (
    DsAggregatePropertyType,
    DsDataSetPropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.metadata_extension import MdMetadataExtensionInformationPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.portrayal_catalogue import MdPortrayalCatalogueReferencePropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.reference_system import MdReferenceSystemPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.spatial_representation import MdSpatialRepresentationPropertyType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataPropertyType:
    class Meta:
        name = "MD_Metadata_PropertyType"

    md_metadata: Optional["MdMetadata"] = field(
        default=None,
        metadata={
            "name": "MD_Metadata",
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
class MdMetadataType(AbstractObjectType):
    """
    Information about the metadata.
    """
    class Meta:
        name = "MD_Metadata_Type"

    file_identifier: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    character_set: Optional[MdCharacterSetCodePropertyType] = field(
        default=None,
        metadata={
            "name": "characterSet",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    parent_identifier: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "parentIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    hierarchy_level: List[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hierarchyLevel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    hierarchy_level_name: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hierarchyLevelName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    date_stamp: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "dateStamp",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    metadata_standard_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataStandardName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    metadata_standard_version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataStandardVersion",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    data_set_uri: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "dataSetURI",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    spatial_representation_info: List[MdSpatialRepresentationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRepresentationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    reference_system_info: List[MdReferenceSystemPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceSystemInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    metadata_extension_info: List[MdMetadataExtensionInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "metadataExtensionInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    identification_info: List[MdIdentificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "identificationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    content_info: List[MdContentInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "contentInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distribution_info: Optional[MdDistributionPropertyType] = field(
        default=None,
        metadata={
            "name": "distributionInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    data_quality_info: List[DqDataQualityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dataQualityInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    portrayal_catalogue_info: List[MdPortrayalCatalogueReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    metadata_constraints: List[MdConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "metadataConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    application_schema_info: List[MdApplicationSchemaInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "applicationSchemaInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    metadata_maintenance: Optional[MdMaintenanceInformationPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataMaintenance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    series: List[DsAggregatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    describes: List[DsDataSetPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    property_type: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "propertyType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    feature_type: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    feature_attribute: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureAttribute",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdMetadata(MdMetadataType):
    class Meta:
        name = "MD_Metadata"
        namespace = "http://www.isotc211.org/2005/gmd"
