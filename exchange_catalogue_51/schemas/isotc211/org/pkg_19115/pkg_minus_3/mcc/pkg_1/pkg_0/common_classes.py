from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    AbstractObjectType,
    CharacterStringPropertyType,
    CodeListValueType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_51.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractConstraintsPropertyType,
    AbstractExtentPropertyType,
    AbstractOnlineResourcePropertyType,
)
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdBrowseGraphicType(AbstractObjectType):
    """
    :ivar file_name: name of the file that contains a graphic that
        provides an illustration of the dataset
    :ivar file_description: text description of the illustration
    :ivar file_type:
    :ivar image_constraints: restriction on access and/or use of browse
        graphic
    :ivar linkage: link to browse graphic
    """
    class Meta:
        name = "MD_BrowseGraphic_Type"

    file_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
            "required": True,
        }
    )
    file_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    file_type: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileType",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    image_constraints: List[AbstractConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "imageConstraints",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    linkage: List[AbstractOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )


@dataclass
class MdIdentifierType(AbstractObjectType):
    """
    :ivar authority: Citation for the code namespace and optionally the
        person or party responsible for maintenance of that namespace
    :ivar code: alphanumeric value identifying an instance in the
        namespace e.g. EPSG::4326
    :ivar code_space: Identifier or namespace in which the code is valid
    :ivar version: version identifier for the namespace
    :ivar description: natural language description of the meaning of
        the code value E.G for codeSpace = EPSG, code = 4326:
        description = WGS-84" to "for codeSpace = EPSG, code =
        EPSG::4326: description = WGS-84
    """
    class Meta:
        name = "MD_Identifier_Type"

    authority: Optional["AbstractCitationPropertyType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    code: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
            "required": True,
        }
    )
    code_space: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )


@dataclass
class MdProgressCode(CodeListValueType):
    """
    Status of the resource.
    """
    class Meta:
        name = "MD_ProgressCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdScopeCode(CodeListValueType):
    """
    Class of information to which the referencing entity applies.
    """
    class Meta:
        name = "MD_ScopeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdScopeDescriptionType(AbstractObjectType):
    """
    :ivar attributes: instances of attribute types to which the
        information applies
    :ivar features: instances of feature types to which the information
        applies
    :ivar feature_instances: feature instances to which the information
        applies
    :ivar attribute_instances: attribute instances to which the
        information applies
    :ivar dataset: dataset to which the information applies
    :ivar other: class of information that does not fall into the other
        categories to which the information applies
    """
    class Meta:
        name = "MD_ScopeDescription_Type"

    attributes: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    features: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    feature_instances: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "featureInstances",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    attribute_instances: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "attributeInstances",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    dataset: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    other: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )


@dataclass
class MdSpatialRepresentationTypeCode(CodeListValueType):
    """
    Method used to represent geographic information in the resource.
    """
    class Meta:
        name = "MD_SpatialRepresentationTypeCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class UriType(AbstractObjectType):
    class Meta:
        name = "URI_Type"


@dataclass
class MdBrowseGraphic(MdBrowseGraphicType):
    """
    Graphic that provides an illustration of the dataset (should include a legend
    for the graphic, if applicable)
    """
    class Meta:
        name = "MD_BrowseGraphic"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdIdentifier(MdIdentifierType):
    """
    Value uniquely identifying an object within a namespace.
    """
    class Meta:
        name = "MD_Identifier"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdProgressCodePropertyType:
    class Meta:
        name = "MD_ProgressCode_PropertyType"

    md_progress_code: Optional[MdProgressCode] = field(
        default=None,
        metadata={
            "name": "MD_ProgressCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class MdScopeCodePropertyType:
    class Meta:
        name = "MD_ScopeCode_PropertyType"

    md_scope_code: Optional[MdScopeCode] = field(
        default=None,
        metadata={
            "name": "MD_ScopeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class MdScopeDescription(MdScopeDescriptionType):
    """
    Description of the class of information covered by the information.
    """
    class Meta:
        name = "MD_ScopeDescription"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdSpatialRepresentationTypeCodePropertyType:
    class Meta:
        name = "MD_SpatialRepresentationTypeCode_PropertyType"

    md_spatial_representation_type_code: Optional[MdSpatialRepresentationTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class Uri(UriType):
    """
    Uniform Resource Identifier (URI), is a compact string of characters used to
    identify or name a resource.
    """
    class Meta:
        name = "URI"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdBrowseGraphicPropertyType:
    class Meta:
        name = "MD_BrowseGraphic_PropertyType"

    md_browse_graphic: Optional[MdBrowseGraphic] = field(
        default=None,
        metadata={
            "name": "MD_BrowseGraphic",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class MdIdentifierPropertyType:
    class Meta:
        name = "MD_Identifier_PropertyType"

    md_identifier: Optional[MdIdentifier] = field(
        default=None,
        metadata={
            "name": "MD_Identifier",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class MdScopeDescriptionPropertyType:
    class Meta:
        name = "MD_ScopeDescription_PropertyType"

    md_scope_description: Optional[MdScopeDescription] = field(
        default=None,
        metadata={
            "name": "MD_ScopeDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class UriPropertyType:
    class Meta:
        name = "URI_PropertyType"

    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
class MdScopeType(AbstractObjectType):
    """
    :ivar level: description of the scope
    :ivar extent:
    :ivar level_description:
    """
    class Meta:
        name = "MD_Scope_Type"

    level: Optional[MdScopeCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
            "required": True,
        }
    )
    extent: List[AbstractExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )
    level_description: List[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "levelDescription",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
        }
    )


@dataclass
class MdScope(MdScopeType):
    """new: information about the scope of the resource"""
    class Meta:
        name = "MD_Scope"
        namespace = "http://standards.iso.org/iso/19115/-3/mcc/1.0"


@dataclass
class MdScopePropertyType:
    class Meta:
        name = "MD_Scope_PropertyType"

    md_scope: Optional[MdScope] = field(
        default=None,
        metadata={
            "name": "MD_Scope",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mcc/1.0",
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
