from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import (
    CodeListValueType,
    NilReasonEnumerationValue,
    TmPeriodDurationPropertyType,
)
from exchange_catalogue_50.schemas.isotc211.org.pkg_19115.pkg_minus_3.mcc.pkg_1.pkg_0.abstract_common_classes import (
    AbstractMaintenanceInformationType,
    AbstractTypedDatePropertyType,
)

__NAMESPACE__ = "http://standards.iso.org/iso/19115/-3/mmi/1.0"


@dataclass
class MdMaintenanceFrequencyCode(CodeListValueType):
    """
    Frequency with which modifications and deletions are made to the data after it
    is first produced.
    """
    class Meta:
        name = "MD_MaintenanceFrequencyCode"
        namespace = "http://standards.iso.org/iso/19115/-3/mmi/1.0"


@dataclass
class MdMaintenanceFrequencyCodePropertyType:
    class Meta:
        name = "MD_MaintenanceFrequencyCode_PropertyType"

    md_maintenance_frequency_code: Optional[MdMaintenanceFrequencyCode] = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceFrequencyCode",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
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
class MdMaintenanceInformationType(AbstractMaintenanceInformationType):
    """
    :ivar maintenance_and_update_frequency: frequency with which changes
        and additions are made to the resource after the initial
        resource is completed
    :ivar maintenance_date: date information associated with maintenance
        of resource
    :ivar user_defined_maintenance_frequency: maintenance period other
        than those defined
    """
    class Meta:
        name = "MD_MaintenanceInformation_Type"

    maintenance_and_update_frequency: Optional[MdMaintenanceFrequencyCodePropertyType] = field(
        default=None,
        metadata={
            "name": "maintenanceAndUpdateFrequency",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
        }
    )
    maintenance_date: List[AbstractTypedDatePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceDate",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
        }
    )
    user_defined_maintenance_frequency: Optional[TmPeriodDurationPropertyType] = field(
        default=None,
        metadata={
            "name": "userDefinedMaintenanceFrequency",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
        }
    )


@dataclass
class MdMaintenanceInformation(MdMaintenanceInformationType):
    """
    Information about the scope and frequency of updating.
    """
    class Meta:
        name = "MD_MaintenanceInformation"
        namespace = "http://standards.iso.org/iso/19115/-3/mmi/1.0"


@dataclass
class MdMaintenanceInformationPropertyType:
    class Meta:
        name = "MD_MaintenanceInformation_PropertyType"

    md_maintenance_information: Optional[MdMaintenanceInformation] = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceInformation",
            "type": "Element",
            "namespace": "http://standards.iso.org/iso/19115/-3/mmi/1.0",
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
