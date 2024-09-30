from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.basic_types import CharacterStringPropertyType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdClassificationCode(CodeListValueType):
    class Meta:
        name = "MD_ClassificationCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdConstraintsType(AbstractObjectType):
    """
    Restrictions on the access and use of a dataset or metadata.
    """
    class Meta:
        name = "MD_Constraints_Type"

    use_limitation: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useLimitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdRestrictionCode(CodeListValueType):
    class Meta:
        name = "MD_RestrictionCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdClassificationCodePropertyType:
    class Meta:
        name = "MD_ClassificationCode_PropertyType"

    md_classification_code: Optional[MdClassificationCode] = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
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
class MdConstraints(MdConstraintsType):
    class Meta:
        name = "MD_Constraints"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRestrictionCodePropertyType:
    class Meta:
        name = "MD_RestrictionCode_PropertyType"

    md_restriction_code: Optional[MdRestrictionCode] = field(
        default=None,
        metadata={
            "name": "MD_RestrictionCode",
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
class MdLegalConstraintsType(MdConstraintsType):
    """
    Restrictions and legal prerequisites for accessing and using the dataset.
    """
    class Meta:
        name = "MD_LegalConstraints_Type"

    access_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "accessConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    use_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    other_constraints: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdSecurityConstraintsType(MdConstraintsType):
    """
    Handling restrictions imposed on the dataset because of national security,
    privacy, or other concerns.
    """
    class Meta:
        name = "MD_SecurityConstraints_Type"

    classification: Optional[MdClassificationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    user_note: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    classification_system: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "classificationSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    handling_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "handlingDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdLegalConstraints(MdLegalConstraintsType):
    class Meta:
        name = "MD_LegalConstraints"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSecurityConstraints(MdSecurityConstraintsType):
    class Meta:
        name = "MD_SecurityConstraints"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdConstraintsPropertyType:
    class Meta:
        name = "MD_Constraints_PropertyType"

    md_security_constraints: Optional[MdSecurityConstraints] = field(
        default=None,
        metadata={
            "name": "MD_SecurityConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_legal_constraints: Optional[MdLegalConstraints] = field(
        default=None,
        metadata={
            "name": "MD_LegalConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    md_constraints: Optional[MdConstraints] = field(
        default=None,
        metadata={
            "name": "MD_Constraints",
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
class MdLegalConstraintsPropertyType:
    class Meta:
        name = "MD_LegalConstraints_PropertyType"

    md_legal_constraints: Optional[MdLegalConstraints] = field(
        default=None,
        metadata={
            "name": "MD_LegalConstraints",
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
class MdSecurityConstraintsPropertyType:
    class Meta:
        name = "MD_SecurityConstraints_PropertyType"

    md_security_constraints: Optional[MdSecurityConstraints] = field(
        default=None,
        metadata={
            "name": "MD_SecurityConstraints",
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
