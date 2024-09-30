from dataclasses import dataclass, field
from typing import Optional, Union
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import NilReasonEnumerationValue
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/gcx/1.0"


@dataclass
class FileNameType:
    class Meta:
        name = "FileName_Type"

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
class MimeFileTypeType:
    class Meta:
        name = "MimeFileType_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AnchorType:
    class Meta:
        name = "Anchor_Type"

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
class FileName(FileNameType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gcx/1.0"


@dataclass
class MimeFileType(MimeFileTypeType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gcx/1.0"


@dataclass
class Anchor(AnchorType):
    class Meta:
        namespace = "http://standards.iso.org/iso/19115/-3/gcx/1.0"


@dataclass
class FileNamePropertyType:
    class Meta:
        name = "FileName_PropertyType"

    file_name: Optional[FileName] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
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
class MimeFileTypePropertyType:
    class Meta:
        name = "MimeFileType_PropertyType"

    mime_file_type: Optional[MimeFileType] = field(
        default=None,
        metadata={
            "name": "MimeFileType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
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
class AnchorPropertyType:
    class Meta:
        name = "Anchor_PropertyType"

    anchor: Optional[Anchor] = field(
        default=None,
        metadata={
            "name": "Anchor",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/gcx/1.0",
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
