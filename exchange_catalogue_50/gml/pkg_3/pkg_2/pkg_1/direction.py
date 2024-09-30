from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    CodeType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import StringOrRefType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.geometry_basic0d1d import Vector
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import ReferenceType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.measures import AngleType
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class CompassPointEnumeration(Enum):
    """These directions are necessarily approximate, giving direction with a
    precision of 22.5°.

    It is thus generally unnecessary to specify the reference frame,
    though this may be detailed in the definition of a GML application
    language.
    """
    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"


@dataclass
class DirectionDescriptionType:
    """Direction descriptions are specified by a compass point code, a keyword, a
    textual description or a reference to a description.

    A gml:compassPoint is specified by a simple enumeration. In
    addition, thre elements to contain text-based descriptions of
    direction are provided. If the direction is specified using a term
    from a list, gml:keyword should be used, and the list indicated
    using the value of the codeSpace attribute. if the direction is
    decribed in prose, gml:direction or gml:reference should be used,
    allowing the value to be included inline or by reference.
    """
    compass_point: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "name": "compassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    keyword: Optional[CodeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    reference: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DirectionVectorType:
    """
    Direction vectors are specified by providing components of a vector.
    """
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    horizontal_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DirectionPropertyType:
    direction_vector: Optional[DirectionVectorType] = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    direction_description: Optional[DirectionDescriptionType] = field(
        default=None,
        metadata={
            "name": "DirectionDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    compass_point: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "name": "CompassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    direction_keyword: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DirectionKeyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    direction_string: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "DirectionString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class Direction(DirectionPropertyType):
    """
    The property gml:direction is intended as a pre-defined property expressing a
    direction to be assigned to features defined in a GML application schema.
    """
    class Meta:
        name = "direction"
        namespace = "http://www.opengis.net/gml/3.2"
