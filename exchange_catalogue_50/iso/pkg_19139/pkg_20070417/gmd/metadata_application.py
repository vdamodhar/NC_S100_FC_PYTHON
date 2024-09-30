from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gco.gco_base import AbstractObjectType
from exchange_catalogue_50.iso.pkg_19139.pkg_20070417.gmd.metadata_entity import MdMetadataPropertyType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsDataSetType(AbstractObjectType):
    """
    Identifiable collection of data.
    """
    class Meta:
        name = "DS_DataSet_Type"

    has: List[MdMetadataPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    part_of: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "partOf",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class DsDataSet(DsDataSetType):
    class Meta:
        name = "DS_DataSet"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsDataSetPropertyType:
    class Meta:
        name = "DS_DataSet_PropertyType"

    ds_data_set: Optional[DsDataSet] = field(
        default=None,
        metadata={
            "name": "DS_DataSet",
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
class AbstractDsAggregateType(AbstractObjectType):
    """
    Identifiable collection of datasets.
    """
    class Meta:
        name = "AbstractDS_Aggregate_Type"

    composed_of: List[DsDataSetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "composedOf",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    series_metadata: List[MdMetadataPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "seriesMetadata",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    subset: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    superset: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class DsInitiativeType(AbstractDsAggregateType):
    class Meta:
        name = "DS_Initiative_Type"


@dataclass
class DsOtherAggregateType(AbstractDsAggregateType):
    class Meta:
        name = "DS_OtherAggregate_Type"


@dataclass
class DsSeriesType(AbstractDsAggregateType):
    class Meta:
        name = "DS_Series_Type"


@dataclass
class DsInitiative(DsInitiativeType):
    class Meta:
        name = "DS_Initiative"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsOtherAggregate(DsOtherAggregateType):
    class Meta:
        name = "DS_OtherAggregate"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsPlatformType(DsSeriesType):
    class Meta:
        name = "DS_Platform_Type"


@dataclass
class DsProductionSeriesType(DsSeriesType):
    class Meta:
        name = "DS_ProductionSeries_Type"


@dataclass
class DsSensorType(DsSeriesType):
    class Meta:
        name = "DS_Sensor_Type"


@dataclass
class DsSeries(DsSeriesType):
    class Meta:
        name = "DS_Series"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsStereoMateType(DsOtherAggregateType):
    class Meta:
        name = "DS_StereoMate_Type"


@dataclass
class DsInitiativePropertyType:
    class Meta:
        name = "DS_Initiative_PropertyType"

    ds_initiative: Optional[DsInitiative] = field(
        default=None,
        metadata={
            "name": "DS_Initiative",
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
class DsPlatform(DsPlatformType):
    class Meta:
        name = "DS_Platform"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsProductionSeries(DsProductionSeriesType):
    class Meta:
        name = "DS_ProductionSeries"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsSensor(DsSensorType):
    class Meta:
        name = "DS_Sensor"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsStereoMate(DsStereoMateType):
    class Meta:
        name = "DS_StereoMate"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAggregatePropertyType:
    class Meta:
        name = "DS_Aggregate_PropertyType"

    ds_initiative: Optional[DsInitiative] = field(
        default=None,
        metadata={
            "name": "DS_Initiative",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_production_series: Optional[DsProductionSeries] = field(
        default=None,
        metadata={
            "name": "DS_ProductionSeries",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_sensor: Optional[DsSensor] = field(
        default=None,
        metadata={
            "name": "DS_Sensor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_platform: Optional[DsPlatform] = field(
        default=None,
        metadata={
            "name": "DS_Platform",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_series: Optional[DsSeries] = field(
        default=None,
        metadata={
            "name": "DS_Series",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_stereo_mate: Optional[DsStereoMate] = field(
        default=None,
        metadata={
            "name": "DS_StereoMate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_other_aggregate: Optional[DsOtherAggregate] = field(
        default=None,
        metadata={
            "name": "DS_OtherAggregate",
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
class DsOtherAggregatePropertyType:
    class Meta:
        name = "DS_OtherAggregate_PropertyType"

    ds_stereo_mate: Optional[DsStereoMate] = field(
        default=None,
        metadata={
            "name": "DS_StereoMate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_other_aggregate: Optional[DsOtherAggregate] = field(
        default=None,
        metadata={
            "name": "DS_OtherAggregate",
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
class DsPlatformPropertyType:
    class Meta:
        name = "DS_Platform_PropertyType"

    ds_platform: Optional[DsPlatform] = field(
        default=None,
        metadata={
            "name": "DS_Platform",
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
class DsProductionSeriesPropertyType:
    class Meta:
        name = "DS_ProductionSeries_PropertyType"

    ds_production_series: Optional[DsProductionSeries] = field(
        default=None,
        metadata={
            "name": "DS_ProductionSeries",
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
class DsSensorPropertyType:
    class Meta:
        name = "DS_Sensor_PropertyType"

    ds_sensor: Optional[DsSensor] = field(
        default=None,
        metadata={
            "name": "DS_Sensor",
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
class DsSeriesPropertyType:
    class Meta:
        name = "DS_Series_PropertyType"

    ds_production_series: Optional[DsProductionSeries] = field(
        default=None,
        metadata={
            "name": "DS_ProductionSeries",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_sensor: Optional[DsSensor] = field(
        default=None,
        metadata={
            "name": "DS_Sensor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_platform: Optional[DsPlatform] = field(
        default=None,
        metadata={
            "name": "DS_Platform",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ds_series: Optional[DsSeries] = field(
        default=None,
        metadata={
            "name": "DS_Series",
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
class DsStereoMatePropertyType:
    class Meta:
        name = "DS_StereoMate_PropertyType"

    ds_stereo_mate: Optional[DsStereoMate] = field(
        default=None,
        metadata={
            "name": "DS_StereoMate",
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
