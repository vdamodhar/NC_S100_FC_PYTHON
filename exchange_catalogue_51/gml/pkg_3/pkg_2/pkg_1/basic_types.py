from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeListType:
    """Gml:CodeListType provides for lists of terms.

    The values in an instance element shall all be valid according to
    the rules of the dictionary, classification scheme, or authority
    identified by the value of its codeSpace attribute.
    """
    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CodeType:
    """Gml:CodeType is a generalized type to be used for a term, keyword or name.

    It adds a XML attribute codeSpace to a term, where the value of the
    codeSpace attribute (if present) shall indicate a dictionary,
    thesaurus, classification scheme, authority, or pattern for the
    term.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinatesType:
    """This type is deprecated for tuples with ordinate values that are numbers.

    CoordinatesType is a text string, intended to be used to record an
    array of tuples or coordinates. While it is not possible to enforce
    the internal structure of the string through schema validation, some
    optional attributes have been provided in previous versions of GML
    to support a description of the internal structure. These attributes
    are deprecated. The attributes were intended to be used as follows:
    Decimal symbol used for a decimal point (default="." a stop or
    period) cs              symbol used to separate components within a
    tuple or coordinate string (default="," a comma) ts
    symbol used to separate tuples or coordinate strings (default=" " a
    space) Since it is based on the XML Schema string type,
    CoordinatesType may be used in the construction of tables of tuples
    or arrays of tuples, including ones that contain mixed text and
    numeric values.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    decimal: str = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    cs: str = field(
        default=",",
        metadata={
            "type": "Attribute",
        }
    )
    ts: str = field(
        default=" ",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MeasureListType:
    """
    Gml:MeasureListType provides for a list of quantities.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )


@dataclass
class MeasureType:
    """Gml:MeasureType supports recording an amount encoded as a value of XML
    Schema double, together with a units of measure indicated by an attribute uom,
    short for "units Of measure".

    The value of the uom attribute identifies a reference system for the
    amount, usually a ratio or interval scale.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )


class NilReasonEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"


class SignType(Enum):
    """
    Gml:SignType is a convenience type with values "+" (plus) and "-" (minus).
    """
    VALUE = "-"
    VALUE_1 = "+"


@dataclass
class CodeOrNilReasonListType:
    """Gml:CodeOrNilReasonListType provides for lists of terms.

    The values in an instance element shall all be valid according to
    the rules of the dictionary, classification scheme, or authority
    identified by the value of its codeSpace attribute. An instance
    element may also include embedded values from NilReasonType. It is
    intended to be used in situations where a term or classification is
    expected, but the value may be absent for some reason.
    """
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CodeWithAuthorityType(CodeType):
    """
    Gml:CodeWithAuthorityType requires that the codeSpace attribute is provided in
    an instance.
    """
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MeasureOrNilReasonListType:
    """Gml:MeasureOrNilReasonListType provides for a list of quantities.

    An instance element may also include embedded values from
    NilReasonType. It is intended to be used in situations where a value
    is expected, but the value may be absent for some reason.
    """
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
