from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from exchange_catalogue_51.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    CharacterStringPropertyType,
    IntegerPropertyType,
)
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gmd.citation import (
    CiOnlineResourcePropertyType,
    CiResponsiblePartyPropertyType,
)
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


class MdObligationCodeType(Enum):
    MANDATORY = "mandatory"
    OPTIONAL = "optional"
    CONDITIONAL = "conditional"


@dataclass
class MdDatatypeCode(CodeListValueType):
    class Meta:
        name = "MD_DatatypeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdObligationCode:
    class Meta:
        name = "MD_ObligationCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdObligationCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MdObligationCodePropertyType:
    class Meta:
        name = "MD_ObligationCode_PropertyType"

    md_obligation_code: Optional[MdObligationCodeType] = field(
        default=None,
        metadata={
            "name": "MD_ObligationCode",
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
class MdDatatypeCodePropertyType:
    class Meta:
        name = "MD_DatatypeCode_PropertyType"

    md_datatype_code: Optional[MdDatatypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DatatypeCode",
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
class MdExtendedElementInformationType(AbstractObjectType):
    """
    New metadata element, not found in ISO 19115, which is required to describe
    geographic data.
    """
    class Meta:
        name = "MD_ExtendedElementInformation_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    short_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    domain_code: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "domainCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    definition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    obligation: Optional[MdObligationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    condition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    data_type: Optional[MdDatatypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    maximum_occurrence: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumOccurrence",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    domain_value: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "domainValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    parent_entity: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "parentEntity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    rule: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    rationale: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class MdExtendedElementInformation(MdExtendedElementInformationType):
    class Meta:
        name = "MD_ExtendedElementInformation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdExtendedElementInformationPropertyType:
    class Meta:
        name = "MD_ExtendedElementInformation_PropertyType"

    md_extended_element_information: Optional[MdExtendedElementInformation] = field(
        default=None,
        metadata={
            "name": "MD_ExtendedElementInformation",
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
class MdMetadataExtensionInformationType(AbstractObjectType):
    """
    Information describing metadata extensions.
    """
    class Meta:
        name = "MD_MetadataExtensionInformation_Type"

    extension_on_line_resource: Optional[CiOnlineResourcePropertyType] = field(
        default=None,
        metadata={
            "name": "extensionOnLineResource",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    extended_element_information: List[MdExtendedElementInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "extendedElementInformation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdMetadataExtensionInformation(MdMetadataExtensionInformationType):
    class Meta:
        name = "MD_MetadataExtensionInformation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataExtensionInformationPropertyType:
    class Meta:
        name = "MD_MetadataExtensionInformation_PropertyType"

    md_metadata_extension_information: Optional[MdMetadataExtensionInformation] = field(
        default=None,
        metadata={
            "name": "MD_MetadataExtensionInformation",
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
