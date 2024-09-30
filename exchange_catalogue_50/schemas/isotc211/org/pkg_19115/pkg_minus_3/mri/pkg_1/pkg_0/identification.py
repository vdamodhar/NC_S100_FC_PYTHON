from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    AnglePropertyType,
    CharacterStringPropertyType,
    CodeListValueType,
    DistancePropertyType,
    IntegerPropertyType,
    NilReasonEnumerationValue,
    TmPeriodDurationPropertyType,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.gmw.pkg_1.pkg_0.gml_wrapper_types import TmPrimitivePropertyType
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.lan.pkg_1.pkg_0.language import PtLocalePropertyType
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractCitationPropertyType,
    AbstractConstraintsPropertyType,
    AbstractExtentPropertyType,
    AbstractFormatPropertyType,
    AbstractMaintenanceInformationPropertyType,
    AbstractResourceDescriptionType,
    AbstractResponsibilityPropertyType,
    AbstractSpatialResolutionType,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.common_classes import (
    MdBrowseGraphicPropertyType,
    MdIdentifierPropertyType,
    MdProgressCodePropertyType,
    MdSpatialRepresentationTypeCodePropertyType,
    UriPropertyType,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/mri/1.0"


class MdTopicCategoryCodeType(Enum):
    """High-level geographic data thematic classification to assist in the grouping
    and search of available geographic data sets.

    Can be used to group keywords as well. Listed examples are not
    exhaustive. NOTE: It is understood there are overlaps between
    general categories and the user is encouraged to select the one most
    appropriate.

    :cvar FARMING: rearing of animals and/or cultivation of
        plantsExamples: agriculture, irrigation, aquaculture,
        plantations, herding, pests and diseases affecting crops and
        livestock
    :cvar BIOTA: flora and/or fauna in natural environment Examples:
        wildlife, vegetation, biological sciences, ecology, wilderness,
        sealife, wetlands, habitat
    :cvar BOUNDARIES: legal land descriptions Examples: political and
        administrative boundaries
    :cvar CLIMATOLOGY_METEOROLOGY_ATMOSPHERE: processes and phenomena of
        the atmosphere Examples: cloud cover, weather, climate,
        atmospheric conditions, climate change, precipitation
    :cvar ECONOMY: economic activities, conditions and employment
        Examples: production, labour, revenue, commerce, industry,
        tourism and ecotourism, forestry, fisheries, commercial or
        subsistence hunting, exploration and exploitation of resources
        such as minerals, oil and gas
    :cvar ELEVATION: height above or below a vertical datumExamples:
        altitude, bathymetry, digital elevation models, slope, derived
        products
    :cvar ENVIRONMENT: environmental resources, protection and
        conservation Examples: environmental pollution, waste storage
        and treatment, environmental impact assessment, monitoring
        environmental risk, nature reserves, landscape
    :cvar GEOSCIENTIFIC_INFORMATION: information pertaining to earth
        sciences Examples: geophysical features and processes, geology,
        minerals, sciences dealing with the composition, structure and
        origin of the earth's rocks, risks of earthquakes, volcanic
        activity, landslides, gravity information, soils, permafrost,
        hydrogeology, erosion
    :cvar HEALTH: health, health services, human ecology, and safety
        Examples: disease and illness, factors affecting health,
        hygiene, substance abuse, mental and physical health, health
        services
    :cvar IMAGERY_BASE_MAPS_EARTH_COVER: base maps Examples: land cover,
        topographic maps, imagery, unclassified images, annotations
    :cvar INTELLIGENCE_MILITARY: military bases, structures, activities
        Examples: barracks, training grounds, military transportation,
        information collection
    :cvar INLAND_WATERS: inland water features, drainage systems and
        their characteristics Examples: rivers and glaciers, salt lakes,
        water utilization plans, dams, currents, floods, water quality,
        hydrographic charts
    :cvar LOCATION: positional information and services Examples:
        addresses, geodetic networks, control points, postal zones and
        services, place names
    :cvar OCEANS: features and characteristics of salt water bodies
        (excluding inland waters) Examples: tides, tidal waves, coastal
        information, reefs
    :cvar PLANNING_CADASTRE: information used for appropriate actions
        for future use of the land Examples: land use maps, zoning maps,
        cadastral surveys, land ownership
    :cvar SOCIETY: characteristics of society and cultures Examples:
        settlements, anthropology, archaeology, education, traditional
        beliefs, manners and customs, demographic data, recreational
        areas and activities, social impact assessments, crime and
        justice, census information
    :cvar STRUCTURE: man-made construction Examples: buildings, museums,
        churches, factories, housing, monuments, shops, towers
    :cvar TRANSPORTATION: means and aids for conveying persons and/or
        goods Examples: roads, airports/airstrips, shipping routes,
        tunnels, nautical charts, vehicle or vessel location,
        aeronautical charts, railways
    :cvar UTILITIES_COMMUNICATION: energy, water and waste systems and
        communications infrastructure and servicesExamples:
        hydroelectricity, geothermal, solar and nuclear sources of
        energy, water purification and distribution, sewage collection
        and disposal, electricity and gas distribution, data
        communication, telecommunication, radio, communication networks
    :cvar EXTRA_TERRESTRIAL: region more than 100 km above the surface
        of the Earth
    :cvar DISASTER:
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
    EXTRA_TERRESTRIAL = "extraTerrestrial"
    DISASTER = "disaster"


@dataclass
class DsAssociationTypeCode(CodeListValueType):
    """
    Justification for the correlation of two resources.
    """
    class Meta:
        name = "DS_AssociationTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class DsInitiativeTypeCode(CodeListValueType):
    """
    Type of aggregation activity in which resources are related.
    """
    class Meta:
        name = "DS_InitiativeTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdKeywordClassType(AbstractObjectType):
    """
    :ivar class_name: character string to label the keyword category in
        natural language
    :ivar concept_identifier: URI of concept in ontology specified by
        the ontology attribute; this concept is labeled by the
        className: CharacterString.
    :ivar ontology: a reference that binds the keyword class to a formal
        conceptualization of a knowledge domain for use in semantic
        processingNOTE: Keywords in the associated MD_Keywords keyword
        list must be within the scope of this ontology
    """
    class Meta:
        name = "MD_KeywordClass_Type"

    class_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "className",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )
    concept_identifier: Optional[UriPropertyType] = field(
        default=None,
        metadata={
            "name": "conceptIdentifier",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    ontology: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )


@dataclass
class MdKeywordTypeCode(CodeListValueType):
    """
    Methods used to group similar keywords.
    """
    class Meta:
        name = "MD_KeywordTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdRepresentativeFractionType(AbstractObjectType):
    """
    :ivar denominator: the number below the line in a vulgar fraction
    """
    class Meta:
        name = "MD_RepresentativeFraction_Type"

    denominator: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )


@dataclass
class MdTopicCategoryCode:
    """High-level geographic data thematic classification to assist in the grouping
    and search of available geographic data sets.

    Can be used to group keywords as well. Listed examples are not
    exhaustive. NOTE: It is understood there are overlaps between
    general categories and the user is encouraged to select the one most
    appropriate.
    """
    class Meta:
        name = "MD_TopicCategoryCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"

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
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdUsageType(AbstractObjectType):
    """
    :ivar specific_usage: brief description of the resource and/or
        resource series usage
    :ivar usage_date_time: date and time of the first use or range of
        uses of the resource and/or resource series
    :ivar user_determined_limitations: applications, determined by the
        user for which the resource and/or resource series is not
        suitable
    :ivar user_contact_info: identification of and means of
        communicating with person(s) and organisation(s) using the
        resource(s)
    :ivar response: response to the user-determined limitationsE.G..
        'this has been fixed in version x'
    :ivar additional_documentation:
    :ivar identified_issues:
    """
    class Meta:
        name = "MD_Usage_Type"

    specific_usage: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )
    usage_date_time: List[TmPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "usageDateTime",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    user_determined_limitations: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userDeterminedLimitations",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    user_contact_info: List[AbstractResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "userContactInfo",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    response: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    additional_documentation: List[AbstractCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "additionalDocumentation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    identified_issues: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "identifiedIssues",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class DsAssociationTypeCodePropertyType:
    class Meta:
        name = "DS_AssociationTypeCode_PropertyType"

    ds_association_type_code: Optional[DsAssociationTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class DsInitiativeTypeCodePropertyType:
    class Meta:
        name = "DS_InitiativeTypeCode_PropertyType"

    ds_initiative_type_code: Optional[DsInitiativeTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_InitiativeTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdKeywordClass(MdKeywordClassType):
    """
    Specification of a class to categorize keywords in a domain-specific vocabulary
    that has a binding to a formal ontology.
    """
    class Meta:
        name = "MD_KeywordClass"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdKeywordTypeCodePropertyType:
    class Meta:
        name = "MD_KeywordTypeCode_PropertyType"

    md_keyword_type_code: Optional[MdKeywordTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdRepresentativeFraction(MdRepresentativeFractionType):
    """
    Derived from ISO 19103 Scale where MD_RepresentativeFraction.denominator = 1 /
    Scale.measure And Scale.targetUnits = Scale.sourceUnits.
    """
    class Meta:
        name = "MD_RepresentativeFraction"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdUsage(MdUsageType):
    """
    Brief description of ways in which the resource(s) is/are currently or has been
    used.
    """
    class Meta:
        name = "MD_Usage"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdAssociatedResourceType(AbstractObjectType):
    """
    :ivar name: citation information about the associated resource
    :ivar association_type: type of relation between the resources
    :ivar initiative_type: type of initiative under which the associated
        resource was produced NOTE: the activity that resulted in the
        associated resource
    :ivar metadata_reference: reference to the metadata of the
        associated resource
    """
    class Meta:
        name = "MD_AssociatedResource_Type"

    name: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    association_type: Optional[DsAssociationTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "associationType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )
    initiative_type: Optional[DsInitiativeTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "initiativeType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    metadata_reference: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataReference",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class MdKeywordClassPropertyType:
    class Meta:
        name = "MD_KeywordClass_PropertyType"

    md_keyword_class: Optional[MdKeywordClass] = field(
        default=None,
        metadata={
            "name": "MD_KeywordClass",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdRepresentativeFractionPropertyType:
    class Meta:
        name = "MD_RepresentativeFraction_PropertyType"

    md_representative_fraction: Optional[MdRepresentativeFraction] = field(
        default=None,
        metadata={
            "name": "MD_RepresentativeFraction",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdUsagePropertyType:
    class Meta:
        name = "MD_Usage_PropertyType"

    md_usage: Optional[MdUsage] = field(
        default=None,
        metadata={
            "name": "MD_Usage",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdAssociatedResource(MdAssociatedResourceType):
    """associated resource information NOTE: An associated resource is a dataset composed of a collection of datasets"""
    class Meta:
        name = "MD_AssociatedResource"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdKeywordsType(AbstractObjectType):
    """
    :ivar keyword: commonly used word(s) or formalised word(s) or
        phrase(s) used to describe the subject
    :ivar type_value: subject matter used to group similar keywords
    :ivar thesaurus_name: name of the formally registered thesaurus or a
        similar authoritative source of keywords
    :ivar keyword_class:
    """
    class Meta:
        name = "MD_Keywords_Type"

    keyword: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "min_occurs": 1,
        }
    )
    type_value: Optional[MdKeywordTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    thesaurus_name: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "thesaurusName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    keyword_class: Optional[MdKeywordClassPropertyType] = field(
        default=None,
        metadata={
            "name": "keywordClass",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class MdResolutionType(AbstractSpatialResolutionType):
    """
    :ivar equivalent_scale: level of detail expressed as the scale of a
        comparable hardcopy map or chart
    :ivar distance: horizontal ground sample distance
    :ivar vertical: Vertical sampling distance
    :ivar angular_distance: Angular sampling measure
    :ivar level_of_detail: brief textual description of the spatial
        resolution of the resource
    """
    class Meta:
        name = "MD_Resolution_Type"

    equivalent_scale: Optional[MdRepresentativeFractionPropertyType] = field(
        default=None,
        metadata={
            "name": "equivalentScale",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    distance: Optional[DistancePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    vertical: Optional[DistancePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    angular_distance: Optional[AnglePropertyType] = field(
        default=None,
        metadata={
            "name": "angularDistance",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    level_of_detail: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "levelOfDetail",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class MdAssociatedResourcePropertyType:
    class Meta:
        name = "MD_AssociatedResource_PropertyType"

    md_associated_resource: Optional[MdAssociatedResource] = field(
        default=None,
        metadata={
            "name": "MD_AssociatedResource",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdKeywords(MdKeywordsType):
    """
    Keywords, their type and reference source NOTE: When the resource described is
    a service, one instance of MD_Keyword shall refer to the service taxonomy
    defined in ISO 19119, 8.3)
    """
    class Meta:
        name = "MD_Keywords"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdResolution(MdResolutionType):
    """
    Level of detail expressed as a scale factor, a distance or an angle.
    """
    class Meta:
        name = "MD_Resolution"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class MdKeywordsPropertyType:
    class Meta:
        name = "MD_Keywords_PropertyType"

    md_keywords: Optional[MdKeywords] = field(
        default=None,
        metadata={
            "name": "MD_Keywords",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdResolutionPropertyType:
    class Meta:
        name = "MD_Resolution_PropertyType"

    md_resolution: Optional[MdResolution] = field(
        default=None,
        metadata={
            "name": "MD_Resolution",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class AbstractMdIdentificationType(AbstractResourceDescriptionType):
    """
    :ivar citation: citation for the resource(s)
    :ivar abstract: brief narrative summary of the content of the
        resource(s)
    :ivar purpose: summary of the intentions with which the resource(s)
        was developed
    :ivar credit: recognition of those who contributed to the
        resource(s)
    :ivar status: status of the resource(s)
    :ivar point_of_contact: identification of, and means of
        communication with, person(s) and organisation(s) associated
        with the resource(s)
    :ivar spatial_representation_type: method used to spatially
        represent geographic information
    :ivar spatial_resolution: factor which provides a general
        understanding of the density of spatial data in the resource
    :ivar temporal_resolution: resolution of the resource with respect
        to time
    :ivar topic_category: main theme(s) of the resource
    :ivar extent: spatial and temporal extent of the resource
    :ivar additional_documentation: other documentation associated with
        the resource
    :ivar processing_level: code that identifies the level of processing
        in the producers coding system of a resource eg. NOAA level 1B
    :ivar resource_maintenance:
    :ivar graphic_overview:
    :ivar resource_format:
    :ivar descriptive_keywords:
    :ivar resource_specific_usage:
    :ivar resource_constraints:
    :ivar associated_resource:
    """
    class Meta:
        name = "AbstractMD_Identification_Type"

    citation: Optional[AbstractCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )
    abstract: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
            "required": True,
        }
    )
    purpose: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    credit: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    status: List[MdProgressCodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    point_of_contact: List[AbstractResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "pointOfContact",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    spatial_representation_type: List[MdSpatialRepresentationTypeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRepresentationType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    spatial_resolution: List[MdResolutionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    temporal_resolution: List[TmPeriodDurationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "temporalResolution",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    topic_category: List[MdTopicCategoryCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "topicCategory",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    extent: List[AbstractExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    additional_documentation: List[AbstractCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "additionalDocumentation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    processing_level: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "processingLevel",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    resource_maintenance: List[AbstractMaintenanceInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceMaintenance",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    graphic_overview: List[MdBrowseGraphicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "graphicOverview",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    resource_format: List[AbstractFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceFormat",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    descriptive_keywords: List[MdKeywordsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "descriptiveKeywords",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    resource_specific_usage: List[MdUsagePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceSpecificUsage",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    resource_constraints: List[AbstractConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    associated_resource: List[MdAssociatedResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "associatedResource",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class MdDataIdentificationType(AbstractMdIdentificationType):
    """
    :ivar default_locale:
    :ivar other_locale:
    :ivar environment_description: description of the resource in the
        producer's processing environment, including items such as the
        software, the computer operating system, file name, and the
        dataset size
    :ivar supplemental_information: any other descriptive information
        about the resource
    """
    class Meta:
        name = "MD_DataIdentification_Type"

    default_locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "name": "defaultLocale",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    other_locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherLocale",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    environment_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "environmentDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    supplemental_information: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "supplementalInformation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )


@dataclass
class MdDataIdentification(MdDataIdentificationType):
    """
    Information required to identify a resource.
    """
    class Meta:
        name = "MD_DataIdentification"
        namespace = "http://standards.iso.org/iso/19115/-3/mri/1.0"


@dataclass
class AbstractMdIdentificationPropertyType:
    class Meta:
        name = "AbstractMD_Identification_PropertyType"

    md_data_identification: Optional[MdDataIdentification] = field(
        default=None,
        metadata={
            "name": "MD_DataIdentification",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
class MdDataIdentificationPropertyType:
    class Meta:
        name = "MD_DataIdentification_PropertyType"

    md_data_identification: Optional[MdDataIdentification] = field(
        default=None,
        metadata={
            "name": "MD_DataIdentification",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
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
