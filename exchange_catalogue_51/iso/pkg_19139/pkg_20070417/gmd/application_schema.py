from dataclasses import dataclass, field
from typing import Optional, Union
from exchange_catalogue_51.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    BinaryPropertyType,
    CharacterStringPropertyType,
)
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.gco_base import AbstractObjectType
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gmd.citation import CiCitationPropertyType
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdApplicationSchemaInformationType(AbstractObjectType):
    """
    Information about the application schema used to build the dataset.
    """
    class Meta:
        name = "MD_ApplicationSchemaInformation_Type"

    name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    schema_language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "schemaLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    constraint_language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "constraintLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    schema_ascii: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "schemaAscii",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    graphics_file: Optional[BinaryPropertyType] = field(
        default=None,
        metadata={
            "name": "graphicsFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    software_development_file: Optional[BinaryPropertyType] = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    software_development_file_format: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFileFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdApplicationSchemaInformation(MdApplicationSchemaInformationType):
    class Meta:
        name = "MD_ApplicationSchemaInformation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdApplicationSchemaInformationPropertyType:
    class Meta:
        name = "MD_ApplicationSchemaInformation_PropertyType"

    md_application_schema_information: Optional[MdApplicationSchemaInformation] = field(
        default=None,
        metadata={
            "name": "MD_ApplicationSchemaInformation",
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
