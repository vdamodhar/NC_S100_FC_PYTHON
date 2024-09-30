from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    CharacterStringPropertyType,
    CodeListValueType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractConstraintsType,
    AbstractResponsibilityPropertyType,
)
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.common_classes import MdScopePropertyType
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdClassificationCode(CodeListValueType):
    """
    Name of the handling restrictions on the resource.
    """
    class Meta:
        name = "MD_ClassificationCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdRestrictionCode(CodeListValueType):
    """
    Limitation(s) placed upon the access or use of the data.
    """
    class Meta:
        name = "MD_RestrictionCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdClassificationCodePropertyType:
    class Meta:
        name = "MD_ClassificationCode_PropertyType"

    md_classification_code: Optional[MdClassificationCode] = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
class MdRestrictionCodePropertyType:
    class Meta:
        name = "MD_RestrictionCode_PropertyType"

    md_restriction_code: Optional[MdRestrictionCode] = field(
        default=None,
        metadata={
            "name": "MD_RestrictionCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
class MdReleasabilityType(AbstractObjectType):
    """
    :ivar addressee: party responsible for the Release statement
    :ivar statement: release statement
    :ivar dissemination_constraints: component in determining
        releasability
    """
    class Meta:
        name = "MD_Releasability_Type"

    addressee: List[AbstractResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    statement: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    dissemination_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "disseminationConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )


@dataclass
class MdReleasability(MdReleasabilityType):
    """
    State, nation or organization to which resource can be released to e.g. NATO
    unclassified releasable to PfP.
    """
    class Meta:
        name = "MD_Releasability"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdReleasabilityPropertyType:
    class Meta:
        name = "MD_Releasability_PropertyType"

    md_releasability: Optional[MdReleasability] = field(
        default=None,
        metadata={
            "name": "MD_Releasability",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
class MdConstraintsType(AbstractConstraintsType):
    """
    :ivar use_limitation: limitation affecting the fitness for use of
        the resource or metadata. Example, "not to be used for
        navigation"
    :ivar constraint_application_scope: Spatial and temporal extent of
        the application of the constraint restrictions
    :ivar graphic: graphic /symbol indicating the constraint Eg.
    :ivar reference: citation/URL for the limitation or constraint, e.g.
        copyright statement, license agreement, etc
    :ivar releasability: information concerning the parties to whom the
        resource can or cannot be released and the party responsible for
        determining the releasibility
    :ivar responsible_party: party responsible for the resource
        constraints
    """
    class Meta:
        name = "MD_Constraints_Type"

    use_limitation: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useLimitation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    constraint_application_scope: Optional[MdScopePropertyType] = field(
        default=None,
        metadata={
            "name": "constraintApplicationScope",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    graphic: List["MdBrowseGraphicPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    reference: List["AbstractCitationPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    releasability: Optional[MdReleasabilityPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    responsible_party: List[AbstractResponsibilityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )


@dataclass
class MdConstraints(MdConstraintsType):
    """
    Restrictions on the access and use of a resource or metadata.
    """
    class Meta:
        name = "MD_Constraints"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdLegalConstraintsType(MdConstraintsType):
    """
    :ivar access_constraints: access constraints applied to assure the
        protection of privacy or intellectual property, and any special
        restrictions or limitations on obtaining the resource or
        metadata
    :ivar use_constraints: constraints applied to assure the protection
        of privacy or intellectual property, and any special
        restrictions or limitations or warnings on using the resource or
        metadata
    :ivar other_constraints: other restrictions and legal prerequisites
        for accessing and using the resource or metadata
    """
    class Meta:
        name = "MD_LegalConstraints_Type"

    access_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "accessConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    use_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    other_constraints: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )


@dataclass
class MdSecurityConstraintsType(MdConstraintsType):
    """
    :ivar classification: name of the handling restrictions on the
        resource or metadata
    :ivar user_note: explanation of the application of the legal
        constraints or other restrictions and legal prerequisites for
        obtaining and using the resource or metadata
    :ivar classification_system: name of the classification system
    :ivar handling_description: additional information about the
        restrictions on handling the resource or metadata
    """
    class Meta:
        name = "MD_SecurityConstraints_Type"

    classification: Optional[MdClassificationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
            "required": True,
        }
    )
    user_note: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userNote",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    classification_system: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "classificationSystem",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    handling_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "handlingDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )


@dataclass
class MdLegalConstraints(MdLegalConstraintsType):
    """
    Restrictions and legal prerequisites for accessing and using the resource or
    metadata.
    """
    class Meta:
        name = "MD_LegalConstraints"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdSecurityConstraints(MdSecurityConstraintsType):
    """
    Handling restrictions imposed on the resource or metadata for national security
    or similar security concerns.
    """
    class Meta:
        name = "MD_SecurityConstraints"
        namespace = "http://standards.iso.org/iso/19115/-3/mco/1.0"


@dataclass
class MdConstraintsPropertyType:
    class Meta:
        name = "MD_Constraints_PropertyType"

    md_security_constraints: Optional[MdSecurityConstraints] = field(
        default=None,
        metadata={
            "name": "MD_SecurityConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    md_legal_constraints: Optional[MdLegalConstraints] = field(
        default=None,
        metadata={
            "name": "MD_LegalConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
        }
    )
    md_constraints: Optional[MdConstraints] = field(
        default=None,
        metadata={
            "name": "MD_Constraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
class MdLegalConstraintsPropertyType:
    class Meta:
        name = "MD_LegalConstraints_PropertyType"

    md_legal_constraints: Optional[MdLegalConstraints] = field(
        default=None,
        metadata={
            "name": "MD_LegalConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
class MdSecurityConstraintsPropertyType:
    class Meta:
        name = "MD_SecurityConstraints_PropertyType"

    md_security_constraints: Optional[MdSecurityConstraints] = field(
        default=None,
        metadata={
            "name": "MD_SecurityConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mco/1.0",
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
