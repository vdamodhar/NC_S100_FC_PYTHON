from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    CharacterStringPropertyType,
    CodeListValueType,
    DateTimePropertyType,
    DatePropertyType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractCitationType,
    AbstractExtentPropertyType,
    AbstractOnlineResourceType,
    AbstractResponsibilityType,
    AbstractTypedDateType,
)
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.common_classes import (
    MdBrowseGraphicPropertyType,
    MdIdentifierPropertyType,
)
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiAddressType(AbstractObjectType):
    """
    :ivar delivery_point: address line for the location (as described in
        ISO 11180, Annex A)
    :ivar city: city of the location
    :ivar administrative_area: state, province of the location
    :ivar postal_code: ZIP or other postal code
    :ivar country: country of the physical address
    :ivar electronic_mail_address: address of the electronic mailbox of
        the responsible organisation or individual
    """
    class Meta:
        name = "CI_Address_Type"

    delivery_point: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "deliveryPoint",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    city: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    administrative_area: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    postal_code: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    country: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    electronic_mail_address: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "electronicMailAddress",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiDateTypeCode(CodeListValueType):
    """
    Identification of when a given event occurred.
    """
    class Meta:
        name = "CI_DateTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiOnLineFunctionCode(CodeListValueType):
    """
    Function performed by the resource.
    """
    class Meta:
        name = "CI_OnLineFunctionCode"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiPresentationFormCode(CodeListValueType):
    """
    Mode in which the data is represented.
    """
    class Meta:
        name = "CI_PresentationFormCode"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiRoleCode(CodeListValueType):
    """
    Function performed by the responsible party.
    """
    class Meta:
        name = "CI_RoleCode"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiSeriesType(AbstractObjectType):
    """
    :ivar name: name of the series, or aggregate resource, of which the
        resource is a part
    :ivar issue_identification: information identifying the issue of the
        series
    :ivar page: details on which pages of the publication the article
        was published
    """
    class Meta:
        name = "CI_Series_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    issue_identification: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "issueIdentification",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    page: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiTelephoneTypeCode(CodeListValueType):
    """
    Type of telephone.
    """
    class Meta:
        name = "CI_TelephoneTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiAddress(CiAddressType):
    """
    Location of the responsible individual or organisation.
    """
    class Meta:
        name = "CI_Address"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiDateTypeCodePropertyType:
    class Meta:
        name = "CI_DateTypeCode_PropertyType"

    ci_date_type_code: Optional[CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiOnLineFunctionCodePropertyType:
    class Meta:
        name = "CI_OnLineFunctionCode_PropertyType"

    ci_on_line_function_code: Optional[CiOnLineFunctionCode] = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiPresentationFormCodePropertyType:
    class Meta:
        name = "CI_PresentationFormCode_PropertyType"

    ci_presentation_form_code: Optional[CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiRoleCodePropertyType:
    class Meta:
        name = "CI_RoleCode_PropertyType"

    ci_role_code: Optional[CiRoleCode] = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiSeries(CiSeriesType):
    """
    Information about the series, or aggregate resource, to which a resource
    belongs.
    """
    class Meta:
        name = "CI_Series"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiTelephoneTypeCodePropertyType:
    class Meta:
        name = "CI_TelephoneTypeCode_PropertyType"

    ci_telephone_type_code: Optional[CiTelephoneTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_TelephoneTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiAddressPropertyType:
    class Meta:
        name = "CI_Address_PropertyType"

    ci_address: Optional[CiAddress] = field(
        default=None,
        metadata={
            "name": "CI_Address",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiDateType(AbstractTypedDateType):
    """
    :ivar date: reference date for the cited resource
    :ivar date_type: event used for reference date
    """
    class Meta:
        name = "CI_Date_Type"

    date: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )
    date_type: Optional[CiDateTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dateType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )


@dataclass
class CiOnlineResourceType(AbstractOnlineResourceType):
    """
    :ivar linkage: location (address) for on-line access using a Uniform
        Resource Locator/Uniform Resource Identifier address or similar
        addressing scheme such as http://www.statkart.no/isotc211
    :ivar protocol: connection protocol to be used e.g. http, ftp, file
    :ivar application_profile: name of an application profile that can
        be used with the online resource
    :ivar name: name of the online resource
    :ivar description: detailed text description of what the online
        resource is/does
    :ivar function: code for function performed by the online resource
    :ivar protocol_request: protocol used by the accessed resource
    """
    class Meta:
        name = "CI_OnlineResource_Type"

    linkage: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )
    protocol: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    application_profile: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "applicationProfile",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    function: Optional[CiOnLineFunctionCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    protocol_request: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "protocolRequest",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiSeriesPropertyType:
    class Meta:
        name = "CI_Series_PropertyType"

    ci_series: Optional[CiSeries] = field(
        default=None,
        metadata={
            "name": "CI_Series",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiTelephoneType(AbstractObjectType):
    """
    :ivar number: telephone number by which individuals can contact
        responsible organisation or individual
    :ivar number_type: type of telephone responsible organisation or
        individual
    """
    class Meta:
        name = "CI_Telephone_Type"

    number: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )
    number_type: Optional[CiTelephoneTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "numberType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiDate(CiDateType):
    """
    Reference date and event used to describe it.
    """
    class Meta:
        name = "CI_Date"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiOnlineResource(CiOnlineResourceType):
    """
    Information about on-line sources from which the resource, specification, or
    community profile name and extended metadata elements can be obtained.
    """
    class Meta:
        name = "CI_OnlineResource"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiTelephone(CiTelephoneType):
    """
    Telephone numbers for contacting the responsible individual or organisation.
    """
    class Meta:
        name = "CI_Telephone"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiDatePropertyType:
    class Meta:
        name = "CI_Date_PropertyType"

    ci_date: Optional[CiDate] = field(
        default=None,
        metadata={
            "name": "CI_Date",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiOnlineResourcePropertyType:
    class Meta:
        name = "CI_OnlineResource_PropertyType"

    ci_online_resource: Optional[CiOnlineResource] = field(
        default=None,
        metadata={
            "name": "CI_OnlineResource",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiTelephonePropertyType:
    class Meta:
        name = "CI_Telephone_PropertyType"

    ci_telephone: Optional[CiTelephone] = field(
        default=None,
        metadata={
            "name": "CI_Telephone",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiContactType(AbstractObjectType):
    """
    :ivar phone: telephone numbers at which the organisation or
        individual may be contacted
    :ivar address: physical and email address at which the organisation
        or individual may be contacted
    :ivar online_resource: on-line information that can be used to
        contact the individual or organisation
    :ivar hours_of_service: time period (including time zone) when
        individuals can contact the organisation or individual
    :ivar contact_instructions: supplemental instructions on how or when
        to contact the individual or organisation
    :ivar contact_type:
    """
    class Meta:
        name = "CI_Contact_Type"

    phone: List[CiTelephonePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    address: List[CiAddressPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    online_resource: List[CiOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "onlineResource",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    hours_of_service: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hoursOfService",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    contact_instructions: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    contact_type: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "contactType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiContact(CiContactType):
    """
    Information required to enable contact with the responsible person and/or
    organisation.
    """
    class Meta:
        name = "CI_Contact"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiContactPropertyType:
    class Meta:
        name = "CI_Contact_PropertyType"

    ci_contact: Optional[CiContact] = field(
        default=None,
        metadata={
            "name": "CI_Contact",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class AbstractCiPartyType(AbstractObjectType):
    """
    :ivar name: name of the party
    :ivar contact_info: contact information for the party
    :ivar party_identifier: value uniquely identifying a party
        (individual or organization)
    """
    class Meta:
        name = "AbstractCI_Party_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    contact_info: List[CiContactPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "contactInfo",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    party_identifier: List[MdIdentifierPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "partyIdentifier",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiIndividualType(AbstractCiPartyType):
    """
    :ivar position_name: position of the individual in an organisation
    """
    class Meta:
        name = "CI_Individual_Type"

    position_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiIndividual(CiIndividualType):
    """
    Information about the party if the party is an individual.
    """
    class Meta:
        name = "CI_Individual"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiIndividualPropertyType:
    class Meta:
        name = "CI_Individual_PropertyType"

    ci_individual: Optional[CiIndividual] = field(
        default=None,
        metadata={
            "name": "CI_Individual",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiOrganisationType(AbstractCiPartyType):
    """
    :ivar logo: Graphic identifying organization
    :ivar individual:
    """
    class Meta:
        name = "CI_Organisation_Type"

    logo: List["MdBrowseGraphicPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    individual: List[CiIndividualPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiOrganisation(CiOrganisationType):
    """
    Information about the party if the party is an organisation.
    """
    class Meta:
        name = "CI_Organisation"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class AbstractCiPartyPropertyType:
    class Meta:
        name = "AbstractCI_Party_PropertyType"

    ci_organisation: Optional[CiOrganisation] = field(
        default=None,
        metadata={
            "name": "CI_Organisation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    ci_individual: Optional[CiIndividual] = field(
        default=None,
        metadata={
            "name": "CI_Individual",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiOrganisationPropertyType:
    class Meta:
        name = "CI_Organisation_PropertyType"

    ci_organisation: Optional[CiOrganisation] = field(
        default=None,
        metadata={
            "name": "CI_Organisation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiResponsibilityType(AbstractResponsibilityType):
    """
    :ivar role: function performed by the responsible party
    :ivar extent: spatial or temporal extent of the role
    :ivar party:
    """
    class Meta:
        name = "CI_Responsibility_Type"

    role: Optional[CiRoleCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )
    extent: List[AbstractExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    party: List[AbstractCiPartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class CiResponsibility(CiResponsibilityType):
    """
    Information about the party and their role.
    """
    class Meta:
        name = "CI_Responsibility"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiResponsibilityPropertyType:
    class Meta:
        name = "CI_Responsibility_PropertyType"

    ci_responsibility: Optional[CiResponsibility] = field(
        default=None,
        metadata={
            "name": "CI_Responsibility",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
class CiCitationType(AbstractCitationType):
    """
    :ivar title: name by which the cited resource is known
    :ivar alternate_title: short name or other language name by which
        the cited information is known. Example: DCW as an alternative
        title for Digital Chart of the World
    :ivar date: reference date for the cited resource
    :ivar edition: version of the cited resource
    :ivar edition_date: date of the edition
    :ivar identifier: value uniquely identifying an object within a
        namespace
    :ivar cited_responsible_party: name and position information for an
        individual or organisation that is responsible for the resource
    :ivar presentation_form: mode in which the resource is represented
    :ivar series: information about the series, or aggregate resource,
        of which the resource is a part
    :ivar other_citation_details: other information required to complete
        the citation that is not recorded elsewhere
    :ivar isbn: international Standard Book Number
    :ivar issn: international Standard Serial Number
    :ivar online_resource: online reference to the cited resource
    :ivar graphic: citation graphic or logo for cited party
    """
    class Meta:
        name = "CI_Citation_Type"

    title: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
            "required": True,
        }
    )
    alternate_title: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "alternateTitle",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    date: List[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    edition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    edition_date: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "editionDate",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    identifier: List[MdIdentifierPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    cited_responsible_party: List[CiResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "citedResponsibleParty",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    presentation_form: List[CiPresentationFormCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "presentationForm",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    series: Optional[CiSeriesPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    other_citation_details: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherCitationDetails",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    isbn: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    issn: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    online_resource: List[CiOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "onlineResource",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )
    graphic: List[MdBrowseGraphicPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
        }
    )


@dataclass
class CiCitation(CiCitationType):
    """
    Standardized resource reference.
    """
    class Meta:
        name = "CI_Citation"
        namespace = "http://standards.iso.org/iso/19115/-3/cit/2.0"


@dataclass
class CiCitationPropertyType:
    class Meta:
        name = "CI_Citation_PropertyType"

    ci_citation: Optional[CiCitation] = field(
        default=None,
        metadata={
            "name": "CI_Citation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/cit/2.0",
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
