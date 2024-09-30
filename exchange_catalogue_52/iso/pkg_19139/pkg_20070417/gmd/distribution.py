from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.basic_types import (
    CharacterStringPropertyType,
    DateTimePropertyType,
    IntegerPropertyType,
    RealPropertyType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gco.gco_base import (
    AbstractObjectType,
    CodeListValueType,
)
from exchange_catalogue_52.iso.pkg_19139.pkg_20070417.gmd.citation import (
    CiOnlineResourcePropertyType,
    CiResponsiblePartyPropertyType,
)
from exchange_catalogue_52.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionUnits(CodeListValueType):
    class Meta:
        name = "MD_DistributionUnits"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributorPropertyType:
    class Meta:
        name = "MD_Distributor_PropertyType"

    md_distributor: Optional["MdDistributor"] = field(
        default=None,
        metadata={
            "name": "MD_Distributor",
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
class MdMediumFormatCode(CodeListValueType):
    class Meta:
        name = "MD_MediumFormatCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumNameCode(CodeListValueType):
    class Meta:
        name = "MD_MediumNameCode"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdStandardOrderProcessType(AbstractObjectType):
    """
    Common ways in which the dataset may be obtained or received, and related
    instructions and fee information.
    """
    class Meta:
        name = "MD_StandardOrderProcess_Type"

    fees: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    planned_available_date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "plannedAvailableDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ordering_instructions: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "orderingInstructions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    turnaround: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdDistributionUnitsPropertyType:
    class Meta:
        name = "MD_DistributionUnits_PropertyType"

    md_distribution_units: Optional[MdDistributionUnits] = field(
        default=None,
        metadata={
            "name": "MD_DistributionUnits",
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
class MdFormatType(AbstractObjectType):
    """
    Description of the form of the data to be distributed.
    """
    class Meta:
        name = "MD_Format_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    amendment_number: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "amendmentNumber",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    specification: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    file_decompression_technique: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileDecompressionTechnique",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    format_distributor: List[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "formatDistributor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdMediumFormatCodePropertyType:
    class Meta:
        name = "MD_MediumFormatCode_PropertyType"

    md_medium_format_code: Optional[MdMediumFormatCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumFormatCode",
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
class MdMediumNameCodePropertyType:
    class Meta:
        name = "MD_MediumNameCode_PropertyType"

    md_medium_name_code: Optional[MdMediumNameCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumNameCode",
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
class MdStandardOrderProcess(MdStandardOrderProcessType):
    class Meta:
        name = "MD_StandardOrderProcess"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFormat(MdFormatType):
    class Meta:
        name = "MD_Format"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumType(AbstractObjectType):
    """
    Information about the media on which the data can be distributed.
    """
    class Meta:
        name = "MD_Medium_Type"

    name: Optional[MdMediumNameCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    density: List[RealPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    density_units: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "densityUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    volumes: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    medium_format: List[MdMediumFormatCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "mediumFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    medium_note: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "mediumNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdStandardOrderProcessPropertyType:
    class Meta:
        name = "MD_StandardOrderProcess_PropertyType"

    md_standard_order_process: Optional[MdStandardOrderProcess] = field(
        default=None,
        metadata={
            "name": "MD_StandardOrderProcess",
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
class MdFormatPropertyType:
    class Meta:
        name = "MD_Format_PropertyType"

    md_format: Optional[MdFormat] = field(
        default=None,
        metadata={
            "name": "MD_Format",
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
class MdMedium(MdMediumType):
    class Meta:
        name = "MD_Medium"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumPropertyType:
    class Meta:
        name = "MD_Medium_PropertyType"

    md_medium: Optional[MdMedium] = field(
        default=None,
        metadata={
            "name": "MD_Medium",
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
class MdDigitalTransferOptionsType(AbstractObjectType):
    """
    Technical means and media by which a dataset is obtained from the distributor.
    """
    class Meta:
        name = "MD_DigitalTransferOptions_Type"

    units_of_distribution: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "unitsOfDistribution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    transfer_size: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "transferSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    on_line: List[CiOnlineResourcePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "onLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    off_line: Optional[MdMediumPropertyType] = field(
        default=None,
        metadata={
            "name": "offLine",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdDigitalTransferOptions(MdDigitalTransferOptionsType):
    class Meta:
        name = "MD_DigitalTransferOptions"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDigitalTransferOptionsPropertyType:
    class Meta:
        name = "MD_DigitalTransferOptions_PropertyType"

    md_digital_transfer_options: Optional[MdDigitalTransferOptions] = field(
        default=None,
        metadata={
            "name": "MD_DigitalTransferOptions",
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
class MdDistributionType(AbstractObjectType):
    """
    Information about the distributor of and options for obtaining the dataset.
    """
    class Meta:
        name = "MD_Distribution_Type"

    distribution_format: List[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distributor: List[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    transfer_options: List[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdDistributorType(AbstractObjectType):
    """
    Information about the distributor.
    """
    class Meta:
        name = "MD_Distributor_Type"

    distributor_contact: Optional[CiResponsiblePartyPropertyType] = field(
        default=None,
        metadata={
            "name": "distributorContact",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    distribution_order_process: List[MdStandardOrderProcessPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionOrderProcess",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distributor_format: List[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributorFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distributor_transfer_options: List[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributorTransferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class MdDistribution(MdDistributionType):
    class Meta:
        name = "MD_Distribution"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributor(MdDistributorType):
    class Meta:
        name = "MD_Distributor"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionPropertyType:
    class Meta:
        name = "MD_Distribution_PropertyType"

    md_distribution: Optional[MdDistribution] = field(
        default=None,
        metadata={
            "name": "MD_Distribution",
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
