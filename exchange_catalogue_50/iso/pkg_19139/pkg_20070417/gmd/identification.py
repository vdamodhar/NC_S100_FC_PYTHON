from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    CharacterStringPropertyType,
    DateTimePropertyType,
    DistancePropertyType,
    IntegerPropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.citation import (
    CiCitationPropertyType,
    CiResponsiblePartyPropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.constraints import MdConstraintsPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.distribution import MdFormatPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.extent import ExExtentPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.maintenance import MdMaintenanceInformationPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.reference_system import MdIdentifierPropertyType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


class MdTopicCategoryCodeType(Enum):
    """
    High-level geospatial data thematic classification to assist in the grouping
    and search of available geospatial datasets.
    """
    FARMING = "farming"
    BIOTA = "biota"
    BOUNDARIES = "boundaries"
    CLIMATOLOGY_METEOROLOGY_ATMOSPHERE = "climatologyMeteorologyAtmosphere"
    ECONOMY = "economy"
    ELEVATION = "elevation"
    ENVIRONMENT = "environment"
    GEOSCIENTIFIC_INFORMATION = "geoscientificInformation"
    HEALTH = "health"
    IMAGERY_BASE_MAPS_EARTH_COVER = "imageryBaseMapsEarthCover"
    INTELLIGENCE_MILITARY = "intelligenceMilitary"
    INLAND_WATERS = "inlandWaters"
    LOCATION = "location"
    OCEANS = "oceans"
    PLANNING_CADASTRE = "planningCadastre"
    SOCIETY = "society"
    STRUCTURE = "structure"
    TRANSPORTATION = "transportation"
    UTILITIES_COMMUNICATION = "utilitiesCommunication"


@dataclass
class DsAssociationTypeCode(CodeListValueType):
    class Meta:
        name = "DS_AssociationTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAssociationType(AbstractObjectType):
    class Meta:
        name = "DS_Association_Type"


@dataclass
class DsInitiativeTypeCode(CodeListValueType):
    class Meta:
        name = "DS_InitiativeTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBrowseGraphicType(AbstractObjectType):
    """
    Graphic that provides an illustration of the dataset (should include a legend
    for the graphic)
    """
    class Meta:
        name = "MD_BrowseGraphic_Type"

    file_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    file_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    file_type: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdCharacterSetCode(CodeListValueType):
    class Meta:
        name = "MD_CharacterSetCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywordTypeCode(CodeListValueType):
    class Meta:
        name = "MD_KeywordTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdProgressCode(CodeListValueType):
    class Meta:
        name = "MD_ProgressCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRepresentativeFractionType(AbstractObjectType):
    class Meta:
        name = "MD_RepresentativeFraction_Type"

    denominator: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )


@dataclass
class MdSpatialRepresentationTypeCode(CodeListValueType):
    class Meta:
        name = "MD_SpatialRepresentationTypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopicCategoryCode:
    class Meta:
        name = "MD_TopicCategoryCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdTopicCategoryCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MdTopicCategoryCodePropertyType:
    class Meta:
        name = "MD_TopicCategoryCode_PropertyType"

    md_topic_category_code: Optional[MdTopicCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
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
class MdUsageType(AbstractObjectType):
    """
    Brief description of ways in which the dataset is currently used.
    """
    class Meta:
        name = "MD_Usage_Type"

    specific_usage: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    usage_date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "usageDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_determined_limitations: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userDeterminedLimitations",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_contact_info: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "userContactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class DsAssociation(DsAssociationType):
    class Meta:
        name = "DS_Association"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAssociationTypeCodePropertyType:
    class Meta:
        name = "DS_AssociationTypeCode_PropertyType"

    ds_association_type_code: Optional[DsAssociationTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
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
class DsInitiativeTypeCodePropertyType:
    class Meta:
        name = "DS_InitiativeTypeCode_PropertyType"

    ds_initiative_type_code: Optional[DsInitiativeTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_InitiativeTypeCode",
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
class MdBrowseGraphic(MdBrowseGraphicType):
    class Meta:
        name = "MD_BrowseGraphic"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCharacterSetCodePropertyType:
    class Meta:
        name = "MD_CharacterSetCode_PropertyType"

    md_character_set_code: Optional[MdCharacterSetCode] = field(
        default=None,
        metadata={
            "name": "MD_CharacterSetCode",
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
class MdKeywordTypeCodePropertyType:
    class Meta:
        name = "MD_KeywordTypeCode_PropertyType"

    md_keyword_type_code: Optional[MdKeywordTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
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
class MdProgressCodePropertyType:
    class Meta:
        name = "MD_ProgressCode_PropertyType"

    md_progress_code: Optional[MdProgressCode] = field(
        default=None,
        metadata={
            "name": "MD_ProgressCode",
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
class MdRepresentativeFraction(MdRepresentativeFractionType):
    class Meta:
        name = "MD_RepresentativeFraction"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSpatialRepresentationTypeCodePropertyType:
    class Meta:
        name = "MD_SpatialRepresentationTypeCode_PropertyType"

    md_spatial_representation_type_code: Optional[MdSpatialRepresentationTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
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
class MdUsage(MdUsageType):
    class Meta:
        name = "MD_Usage"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAssociationPropertyType:
    class Meta:
        name = "DS_Association_PropertyType"

    ds_association: Optional[DsAssociation] = field(
        default=None,
        metadata={
            "name": "DS_Association",
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
class MdAggregateInformationType(AbstractObjectType):
    """
    Encapsulates the dataset aggregation information.
    """
    class Meta:
        name = "MD_AggregateInformation_Type"

    aggregate_data_set_name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "aggregateDataSetName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    aggregate_data_set_identifier: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "aggregateDataSetIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    association_type: Optional[DsAssociationTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "associationType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    initiative_type: Optional[DsInitiativeTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "initiativeType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdBrowseGraphicPropertyType:
    class Meta:
        name = "MD_BrowseGraphic_PropertyType"

    md_browse_graphic: Optional[MdBrowseGraphic] = field(
        default=None,
        metadata={
            "name": "MD_BrowseGraphic",
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
class MdKeywordsType(AbstractObjectType):
    """
    Keywords, their type and reference source.
    """
    class Meta:
        name = "MD_Keywords_Type"

    keyword: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    type_value: Optional[MdKeywordTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    thesaurus_name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "thesaurusName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdRepresentativeFractionPropertyType:
    class Meta:
        name = "MD_RepresentativeFraction_PropertyType"

    md_representative_fraction: Optional[MdRepresentativeFraction] = field(
        default=None,
        metadata={
            "name": "MD_RepresentativeFraction",
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
class MdUsagePropertyType:
    class Meta:
        name = "MD_Usage_PropertyType"

    md_usage: Optional[MdUsage] = field(
        default=None,
        metadata={
            "name": "MD_Usage",
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
class MdAggregateInformation(MdAggregateInformationType):
    class Meta:
        name = "MD_AggregateInformation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywords(MdKeywordsType):
    class Meta:
        name = "MD_Keywords"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdResolutionType:
    class Meta:
        name = "MD_Resolution_Type"

    equivalent_scale: Optional[MdRepresentativeFractionPropertyType] = field(
        default=None,
        metadata={
            "name": "equivalentScale",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distance: Optional[DistancePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdAggregateInformationPropertyType:
    class Meta:
        name = "MD_AggregateInformation_PropertyType"

    md_aggregate_information: Optional[MdAggregateInformation] = field(
        default=None,
        metadata={
            "name": "MD_AggregateInformation",
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
class MdKeywordsPropertyType:
    class Meta:
        name = "MD_Keywords_PropertyType"

    md_keywords: Optional[MdKeywords] = field(
        default=None,
        metadata={
            "name": "MD_Keywords",
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
class MdResolution(MdResolutionType):
    class Meta:
        name = "MD_Resolution"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdIdentificationType(AbstractObjectType):
    """
    Basic information about data.
    """
    class Meta:
        name = "AbstractMD_Identification_Type"

    citation: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    abstract: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    purpose: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    credit: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    status: List[MdProgressCodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    point_of_contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "pointOfContact",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    resource_maintenance: List[MdMaintenanceInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceMaintenance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    graphic_overview: List[MdBrowseGraphicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "graphicOverview",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    resource_format: List[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    descriptive_keywords: List[MdKeywordsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "descriptiveKeywords",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    resource_specific_usage: List[MdUsagePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceSpecificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    resource_constraints: List[MdConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    aggregation_info: List[MdAggregateInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "aggregationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdResolutionPropertyType:
    class Meta:
        name = "MD_Resolution_PropertyType"

    md_resolution: Optional[MdResolution] = field(
        default=None,
        metadata={
            "name": "MD_Resolution",
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
class MdDataIdentificationType(AbstractMdIdentificationType):
    class Meta:
        name = "MD_DataIdentification_Type"

    spatial_representation_type: List[MdSpatialRepresentationTypeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRepresentationType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    spatial_resolution: List[MdResolutionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    language: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    character_set: List[MdCharacterSetCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "characterSet",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    topic_category: List[MdTopicCategoryCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "topicCategory",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    environment_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "environmentDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    extent: List[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    supplemental_information: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "supplementalInformation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdServiceIdentificationType(AbstractMdIdentificationType):
    """
    See 19119 for further info.
    """
    class Meta:
        name = "MD_ServiceIdentification_Type"


@dataclass
class MdDataIdentification(MdDataIdentificationType):
    class Meta:
        name = "MD_DataIdentification"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdServiceIdentification(MdServiceIdentificationType):
    class Meta:
        name = "MD_ServiceIdentification"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDataIdentificationPropertyType:
    class Meta:
        name = "MD_DataIdentification_PropertyType"

    md_data_identification: Optional[MdDataIdentification] = field(
        default=None,
        metadata={
            "name": "MD_DataIdentification",
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
class MdIdentificationPropertyType:
    class Meta:
        name = "MD_Identification_PropertyType"

    md_service_identification: Optional[MdServiceIdentification] = field(
        default=None,
        metadata={
            "name": "MD_ServiceIdentification",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_data_identification: Optional[MdDataIdentification] = field(
        default=None,
        metadata={
            "name": "MD_DataIdentification",
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
class MdServiceIdentificationPropertyType:
    class Meta:
        name = "MD_ServiceIdentification_PropertyType"

    md_service_identification: Optional[MdServiceIdentification] = field(
        default=None,
        metadata={
            "name": "MD_ServiceIdentification",
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
