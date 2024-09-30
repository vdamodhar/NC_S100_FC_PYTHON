from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.cit.pkg_1.pkg_0.citation import (
    CiDatePropertyType,
    CiResponsibilityPropertyType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    CharacterStringPropertyType,
    CodeListValueType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class LocalisedCharacterStringType:
    class Meta:
        name = "LocalisedCharacterString_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CountryCode(CodeListValueType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class LanguageCode(CodeListValueType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class LocalisedCharacterString(LocalisedCharacterStringType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class MdCharacterSetCode(CodeListValueType):
    class Meta:
        name = "MD_CharacterSetCode"
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class CountryCodePropertyType:
    class Meta:
        name = "CountryCode_PropertyType"

    country_code: Optional[CountryCode] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
class LanguageCodePropertyType:
    class Meta:
        name = "LanguageCode_PropertyType"

    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
class LocalisedCharacterStringPropertyType:
    class Meta:
        name = "LocalisedCharacterString_PropertyType"

    localised_character_string: Optional[LocalisedCharacterString] = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
class MdCharacterSetCodePropertyType:
    class Meta:
        name = "MD_CharacterSetCode_PropertyType"

    md_character_set_code: Optional[MdCharacterSetCode] = field(
        default=None,
        metadata={
            "name": "MD_CharacterSetCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
class PtFreeTextType(AbstractObjectType):
    class Meta:
        name = "PT_FreeText_Type"

    text_group: List[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "textGroup",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class PtLocaleType(AbstractObjectType):
    class Meta:
        name = "PT_Locale_Type"

    language: Optional[LanguageCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "required": True,
        }
    )
    country: Optional[CountryCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    character_encoding: Optional[MdCharacterSetCodePropertyType] = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "required": True,
        }
    )


@dataclass
class PtFreeText(PtFreeTextType):
    class Meta:
        name = "PT_FreeText"
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class PtLocale(PtLocaleType):
    class Meta:
        name = "PT_Locale"
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class PtLocaleContainerType(PtLocaleType):
    class Meta:
        name = "PT_LocaleContainer_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "required": True,
        }
    )
    locale: Optional["PtLocalePropertyType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "required": True,
        }
    )
    date: List[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "min_occurs": 1,
        }
    )
    responsible_party: List[CiResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "min_occurs": 1,
        }
    )
    localised_string: List[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "localisedString",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class PtFreeTextPropertyType(CharacterStringPropertyType):
    class Meta:
        name = "PT_FreeText_PropertyType"

    pt_free_text: Optional[PtFreeText] = field(
        default=None,
        metadata={
            "name": "PT_FreeText",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )


@dataclass
class PtLocaleContainer(PtLocaleContainerType):
    class Meta:
        name = "PT_LocaleContainer"
        namespace = "http://standards.iso.org/iso/19115/-3/lan/1.0"


@dataclass
class PtLocaleContainerPropertyType:
    class Meta:
        name = "PT_LocaleContainer_PropertyType"

    pt_locale_container: Optional[PtLocaleContainer] = field(
        default=None,
        metadata={
            "name": "PT_LocaleContainer",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
class PtLocalePropertyType:
    class Meta:
        name = "PT_Locale_PropertyType"

    pt_locale_container: Optional[PtLocaleContainer] = field(
        default=None,
        metadata={
            "name": "PT_LocaleContainer",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    pt_locale: Optional[PtLocale] = field(
        default=None,
        metadata={
            "name": "PT_Locale",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
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
