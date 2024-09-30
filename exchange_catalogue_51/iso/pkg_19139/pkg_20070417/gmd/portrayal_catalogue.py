from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_51.gml.pkg_3.pkg_2.pkg_1.basic_types import NilReasonEnumerationValue
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gco.gco_base import AbstractObjectType
from exchange_catalogue_51.iso.pkg_19139.pkg_20070417.gmd.citation import CiCitationPropertyType
from exchange_catalogue_51.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReferenceType(AbstractObjectType):
    """
    Information identifing the portrayal catalogue used.
    """
    class Meta:
        name = "MD_PortrayalCatalogueReference_Type"

    portrayal_catalogue_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )


@dataclass
class MdPortrayalCatalogueReference(MdPortrayalCatalogueReferenceType):
    class Meta:
        name = "MD_PortrayalCatalogueReference"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReferencePropertyType:
    class Meta:
        name = "MD_PortrayalCatalogueReference_PropertyType"

    md_portrayal_catalogue_reference: Optional[MdPortrayalCatalogueReference] = field(
        default=None,
        metadata={
            "name": "MD_PortrayalCatalogueReference",
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
