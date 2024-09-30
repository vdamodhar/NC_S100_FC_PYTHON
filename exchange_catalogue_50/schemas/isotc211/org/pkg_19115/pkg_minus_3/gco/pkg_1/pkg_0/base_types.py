from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod
from exchange_catalogue_50.s100.pkg_5.pkg_0.pkg_0.s100_catalog.pkg_20220705.maintenance import MdMaintenanceFrequencyCode
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.cit.pkg_1.pkg_0.citation import (
    CiDateTypeCode as Type1CiDateTypeCode,
    CiOnLineFunctionCode as Type1CiOnLineFunctionCode,
    CiPresentationFormCode as Type1CiPresentationFormCode,
    CiRoleCode as Type1CiRoleCode,
    CiTelephoneTypeCode as Type1CiTelephoneTypeCode,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.cit.pkg_2.pkg_0.citation import (
    CiDateTypeCode as Type2CiDateTypeCode,
    CiOnLineFunctionCode as Type2CiOnLineFunctionCode,
    CiPresentationFormCode as Type2CiPresentationFormCode,
    CiRoleCode as Type2CiRoleCode,
    CiTelephoneTypeCode as Type2CiTelephoneTypeCode,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.gcx.pkg_1.pkg_0.extended_types import (
    Anchor,
    FileName,
    MimeFileType,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.lan.pkg_1.pkg_0.language import (
    CountryCode,
    LanguageCode,
    LocalisedCharacterString,
    MdCharacterSetCode,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.common_classes import (
    MdProgressCode,
    MdScopeCode,
    MdSpatialRepresentationTypeCode,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mco.pkg_1.pkg_0.constraints import (
    MdClassificationCode,
    MdRestrictionCode,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mri.pkg_1.pkg_0.identification import (
    DsAssociationTypeCode,
    DsInitiativeTypeCode,
    MdKeywordTypeCode,
    MdTopicCategoryCodeType,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class AbstractObjectType:
    class Meta:
        name = "AbstractObject_Type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BinaryType:
    class Meta:
        name = "Binary_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Boolean:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CharacterString:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class CodeListValueType:
    class Meta:
        name = "CodeListValue_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeList",
            "type": "Attribute",
            "required": True,
        }
    )
    code_list_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeListValue",
            "type": "Attribute",
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CodeType:
    """Gml:CodeType is a generalized type to be used for a term, keyword or name.

    It adds a XML attribute codeSpace to a term, where the value of the
    codeSpace attribute (if present) shall indicate a dictionary,
    thesaurus, classification scheme, authority, or pattern for the
    term.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class Date:
    class Meta:
        nillable = True
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "nillable": True,
        }
    )


@dataclass
class DateTime:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DecimalType:
    class Meta:
        name = "Decimal"
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Integer:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MeasureType:
    """Copied from gml32:MeasureType, which supports recording an amount encoded as
    a value of XML Schema double, together with a units of measure indicated by an
    attribute uom, short for "units Of measure".

    The value of the uom attribute identifies a reference system for the
    amount, usually a ratio or interval scale. Namespace changed to gco
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )


class NilReasonEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"


@dataclass
class Real:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Record:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class TmPeriodDuration:
    class Meta:
        name = "TM_PeriodDuration"
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class UnlimitedIntegerType:
    class Meta:
        name = "UnlimitedInteger_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    is_infinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isInfinite",
            "type": "Attribute",
        }
    )


@dataclass
class UomIdentifier:
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[^: \n\r\t]+",
        }
    )


@dataclass
class Angle(MeasureType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class Binary(BinaryType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class BooleanPropertyType:
    class Meta:
        name = "Boolean_PropertyType"

    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class CharacterStringPropertyType:
    class Meta:
        name = "CharacterString_PropertyType"

    md_topic_category_code: Optional[MdTopicCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    md_keyword_type_code: Optional[MdKeywordTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    ds_initiative_type_code: Optional[DsInitiativeTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_InitiativeTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    ds_association_type_code: Optional[DsAssociationTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mri/1.0",
        }
    )
    md_restriction_code: Optional[MdRestrictionCode] = field(
        default=None,
        metadata={
            "name": "MD_RestrictionCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    md_classification_code: Optional[MdClassificationCode] = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    md_character_set_code: Optional[MdCharacterSetCode] = field(
        default=None,
        metadata={
            "name": "MD_CharacterSetCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    localised_character_string: Optional[LocalisedCharacterString] = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    country_code: Optional[CountryCode] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/lan/1.0",
        }
    )
    ci_telephone_type_code: Optional[Type1CiTelephoneTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_TelephoneTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/1.0",
        }
    )
    ci_role_code: Optional[Type1CiRoleCode] = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/1.0",
        }
    )
    ci_presentation_form_code: Optional[Type1CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/1.0",
        }
    )
    ci_on_line_function_code: Optional[Type1CiOnLineFunctionCode] = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/1.0",
        }
    )
    ci_date_type_code: Optional[Type1CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/1.0",
        }
    )
    anchor: Optional[Anchor] = field(
        default=None,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
        }
    )
    mime_file_type: Optional[MimeFileType] = field(
        default=None,
        metadata={
            "name": "MimeFileType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
        }
    )
    file_name: Optional[FileName] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
        }
    )
    standards_iso_org_iso_19115_3_cit_2_0_ci_telephone_type_code: Optional[Type2CiTelephoneTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_TelephoneTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    standards_iso_org_iso_19115_3_cit_2_0_ci_role_code: Optional[Type2CiRoleCode] = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    standards_iso_org_iso_19115_3_cit_2_0_ci_presentation_form_code: Optional[Type2CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    standards_iso_org_iso_19115_3_cit_2_0_ci_on_line_function_code: Optional[Type2CiOnLineFunctionCode] = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    standards_iso_org_iso_19115_3_cit_2_0_ci_date_type_code: Optional[Type2CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    md_maintenance_frequency_code: Optional[MdMaintenanceFrequencyCode] = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceFrequencyCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
        }
    )
    md_spatial_representation_type_code: Optional[MdSpatialRepresentationTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    md_scope_code: Optional[MdScopeCode] = field(
        default=None,
        metadata={
            "name": "MD_ScopeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    md_progress_code: Optional[MdProgressCode] = field(
        default=None,
        metadata={
            "name": "MD_ProgressCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    character_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacterString",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class DateTimePropertyType:
    class Meta:
        name = "DateTime_PropertyType"

    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class DatePropertyType:
    class Meta:
        name = "Date_PropertyType"

    date: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "nillable": True,
        }
    )
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class DecimalPropertyType:
    class Meta:
        name = "Decimal_PropertyType"

    decimal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Decimal",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class Distance(MeasureType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class IntegerPropertyType:
    class Meta:
        name = "Integer_PropertyType"

    integer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class Length(MeasureType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class Measure(MeasureType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class NumberPropertyType:
    class Meta:
        name = "Number_PropertyType"

    real: Optional[float] = field(
        default=None,
        metadata={
            "name": "Real",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    decimal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Decimal",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    integer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class ObjectReferencePropertyType:
    class Meta:
        name = "ObjectReference_PropertyType"

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
class RealPropertyType:
    class Meta:
        name = "Real_PropertyType"

    real: Optional[float] = field(
        default=None,
        metadata={
            "name": "Real",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class RecordTypeType:
    class Meta:
        name = "RecordType_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
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


@dataclass
class RecordPropertyType:
    class Meta:
        name = "Record_PropertyType"

    record: Optional[Record] = field(
        default=None,
        metadata={
            "name": "Record",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class ScopedName(CodeType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class TmPeriodDurationPropertyType:
    class Meta:
        name = "TM_PeriodDuration_PropertyType"

    tm_period_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TM_PeriodDuration",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class UnlimitedInteger(UnlimitedIntegerType):
    class Meta:
        nillable = True
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class UomIdentifierPropertyType:
    class Meta:
        name = "UomIdentifier_PropertyType"

    uom_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "UomIdentifier",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"[^: \n\r\t]+",
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
class AnglePropertyType:
    class Meta:
        name = "Angle_PropertyType"

    angle: Optional[Angle] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class BinaryPropertyType:
    class Meta:
        name = "Binary_PropertyType"

    binary: Optional[Binary] = field(
        default=None,
        metadata={
            "name": "Binary",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class DistancePropertyType:
    class Meta:
        name = "Distance_PropertyType"

    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class GenericNamePropertyType:
    class Meta:
        name = "GenericName_PropertyType"

    scoped_name: Optional[ScopedName] = field(
        default=None,
        metadata={
            "name": "ScopedName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class LengthPropertyType:
    class Meta:
        name = "Length_PropertyType"

    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    length: Optional[Length] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class MeasurePropertyType:
    class Meta:
        name = "Measure_PropertyType"

    angle: Optional[Angle] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    length: Optional[Length] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
        }
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class RecordType(RecordTypeType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class ScopedNamePropertyType:
    class Meta:
        name = "ScopedName_PropertyType"

    scoped_name: Optional[ScopedName] = field(
        default=None,
        metadata={
            "name": "ScopedName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class TypeNameType(AbstractObjectType):
    """A TypeName is a LocalName that references either a recordType or object type
    in some form of schema.

    The stored value "aName" is the returned value for the "aName()" operation. This is the types name.  - For parsing from types (or objects) the parsible name normally uses a "." navigation separator, so that it is of the form  [class].[member].[memberOfMember]. ...)
    """
    class Meta:
        name = "TypeName_Type"

    a_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "aName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "required": True,
        }
    )


@dataclass
class UnlimitedIntegerPropertyType:
    class Meta:
        name = "UnlimitedInteger_PropertyType"

    unlimited_integer: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "UnlimitedInteger",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "nillable": True,
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
class MultiplicityRangeType(AbstractObjectType):
    """
    A component of a multiplicity, consisting of an non-negative lower bound, and a
    potentially infinite upper bound.
    """
    class Meta:
        name = "MultiplicityRange_Type"

    lower: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "required": True,
        }
    )
    upper: Optional[UnlimitedIntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "required": True,
        }
    )


@dataclass
class RecordTypePropertyType:
    class Meta:
        name = "RecordType_PropertyType"

    record_type: Optional[RecordType] = field(
        default=None,
        metadata={
            "name": "RecordType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class TypeName(TypeNameType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class MultiplicityRange(MultiplicityRangeType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class TypeNamePropertyType:
    class Meta:
        name = "TypeName_PropertyType"

    type_name: Optional[TypeName] = field(
        default=None,
        metadata={
            "name": "TypeName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class MemberNameType(AbstractObjectType):
    """A MemberName is a LocalName that references either an attribute slot in a
    record or  recordType or an attribute, operation, or association role in an
    object instance or  type description in some form of schema.

    The stored value "aName" is the returned value for the "aName()"
    operation.
    """
    class Meta:
        name = "MemberName_Type"

    a_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "aName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "required": True,
        }
    )
    attribute_type: Optional[TypeNamePropertyType] = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "required": True,
        }
    )


@dataclass
class MultiplicityRangePropertyType:
    class Meta:
        name = "MultiplicityRange_PropertyType"

    multiplicity_range: Optional[MultiplicityRange] = field(
        default=None,
        metadata={
            "name": "MultiplicityRange",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class MemberName(MemberNameType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class MultiplicityType(AbstractObjectType):
    """Use to represent the possible cardinality of a relation.

    Represented by a set of simple multiplicity ranges.
    """
    class Meta:
        name = "Multiplicity_Type"

    range: List[MultiplicityRangePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class MemberNamePropertyType:
    class Meta:
        name = "MemberName_PropertyType"

    member_name: Optional[MemberName] = field(
        default=None,
        metadata={
            "name": "MemberName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
class Multiplicity(MultiplicityType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gco/1.0"


@dataclass
class MultiplicityPropertyType:
    class Meta:
        name = "Multiplicity_PropertyType"

    multiplicity: Optional[Multiplicity] = field(
        default=None,
        metadata={
            "name": "Multiplicity",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
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
