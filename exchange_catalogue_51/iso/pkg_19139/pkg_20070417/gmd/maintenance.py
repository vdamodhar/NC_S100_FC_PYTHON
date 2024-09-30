from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_51.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    CharacterStringPropertyType,
    DatePropertyType,
)
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
    ObjectReferencePropertyType,
)
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gmd.citation import CiResponsiblePartyPropertyType
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gts.temporal_objects import TmPeriodDurationPropertyType
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceFrequencyCode(CodeListValueType):
    class Meta:
        name = "MD_MaintenanceFrequencyCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeCode(CodeListValueType):
    class Meta:
        name = "MD_ScopeCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionType:
    """
    Description of the class of information covered by the information.
    """
    class Meta:
        name = "MD_ScopeDescription_Type"

    attributes: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    features: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    feature_instances: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    attribute_instances: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "attributeInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dataset: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    other: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdMaintenanceFrequencyCodePropertyType:
    class Meta:
        name = "MD_MaintenanceFrequencyCode_PropertyType"

    md_maintenance_frequency_code: Optional[MdMaintenanceFrequencyCode] = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceFrequencyCode",
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
class MdScopeCodePropertyType:
    class Meta:
        name = "MD_ScopeCode_PropertyType"

    md_scope_code: Optional[MdScopeCode] = field(
        default=None,
        metadata={
            "name": "MD_ScopeCode",
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
class MdScopeDescription(MdScopeDescriptionType):
    class Meta:
        name = "MD_ScopeDescription"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionPropertyType:
    class Meta:
        name = "MD_ScopeDescription_PropertyType"

    md_scope_description: Optional[MdScopeDescription] = field(
        default=None,
        metadata={
            "name": "MD_ScopeDescription",
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
class MdMaintenanceInformationType(AbstractObjectType):
    """
    Information about the scope and frequency of updating.
    """
    class Meta:
        name = "MD_MaintenanceInformation_Type"

    maintenance_and_update_frequency: Optional[MdMaintenanceFrequencyCodePropertyType] = field(
        default=None,
        metadata={
            "name": "maintenanceAndUpdateFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    date_of_next_update: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "dateOfNextUpdate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_defined_maintenance_frequency: Optional[TmPeriodDurationPropertyType] = field(
        default=None,
        metadata={
            "name": "userDefinedMaintenanceFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    update_scope: List[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScope",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    update_scope_description: List[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    maintenance_note: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdMaintenanceInformation(MdMaintenanceInformationType):
    class Meta:
        name = "MD_MaintenanceInformation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceInformationPropertyType:
    class Meta:
        name = "MD_MaintenanceInformation_PropertyType"

    md_maintenance_information: Optional[MdMaintenanceInformation] = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceInformation",
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
