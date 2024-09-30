from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.basic_types import CharacterStringPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
    ObjectReferencePropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.citation import (
    CiDatePropertyType,
    CiResponsiblePartyPropertyType,
)
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.identification import MdCharacterSetCodePropertyType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


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
class Country(CodeListValueType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LanguageCode(CodeListValueType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LocalisedCharacterString(LocalisedCharacterStringType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class CountryPropertyType:
    class Meta:
        name = "Country_PropertyType"

    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
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
class LanguageCodePropertyType:
    class Meta:
        name = "LanguageCode_PropertyType"

    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
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
class LocalisedCharacterStringPropertyType(ObjectReferencePropertyType):
    class Meta:
        name = "LocalisedCharacterString_PropertyType"

    localised_character_string: Optional[LocalisedCharacterString] = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class PtLocaleType(AbstractObjectType):
    class Meta:
        name = "PT_Locale_Type"

    language_code: Optional[LanguageCodePropertyType] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    country: Optional[CountryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    character_encoding: Optional[MdCharacterSetCodePropertyType] = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )


@dataclass
class PtFreeText(PtFreeTextType):
    class Meta:
        name = "PT_FreeText"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocale(PtLocaleType):
    class Meta:
        name = "PT_Locale"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtFreeTextPropertyType(CharacterStringPropertyType):
    class Meta:
        name = "PT_FreeText_PropertyType"

    pt_free_text: Optional[PtFreeText] = field(
        default=None,
        metadata={
            "name": "PT_FreeText",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class PtLocalePropertyType:
    class Meta:
        name = "PT_Locale_PropertyType"

    pt_locale: Optional[PtLocale] = field(
        default=None,
        metadata={
            "name": "PT_Locale",
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
class PtLocaleContainerType:
    class Meta:
        name = "PT_LocaleContainer_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    date: List[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    responsible_party: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    localised_string: List[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "localisedString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class PtLocaleContainer(PtLocaleContainerType):
    class Meta:
        name = "PT_LocaleContainer"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleContainerPropertyType:
    class Meta:
        name = "PT_LocaleContainer_PropertyType"

    pt_locale_container: Optional[PtLocaleContainer] = field(
        default=None,
        metadata={
            "name": "PT_LocaleContainer",
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
