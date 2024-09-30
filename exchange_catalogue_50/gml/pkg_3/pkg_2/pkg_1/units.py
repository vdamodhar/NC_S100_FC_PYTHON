from dataclasses import dataclass, field
from typing import List, Optional
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import CodeType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import StringOrRefType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.dictionary import DefinitionType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class FormulaType:
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class UnitOfMeasureType:
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )


@dataclass
class ConversionToPreferredUnitType(UnitOfMeasureType):
    """The inherited attribute uom references the preferred unit that this
    conversion applies to. The conversion of a unit to the preferred unit for this
    physical quantity type is specified by an arithmetic conversion (scaling and/or
    offset). The content model extends gml:UnitOfMeasureType, which has a mandatory
    attribute uom which identifies the preferred unit for the physical quantity
    type that this conversion applies to. The conversion is specified by a choice
    of.

    -       gml:factor, which defines the scale factor, or
    -       gml:formula, which defines a formula
    by which a value using the conventional unit of measure can be converted to obtain the corresponding value using the preferred unit of measure.
    The formula defines the parameters of a simple formula by which a value using the conventional unit of measure can be converted to the corresponding value using the preferred unit of measure. The formula element contains elements a, b, c and d, whose values use the XML Schema type double. These values are used in the formula y = (a + bx) / (c + dx), where x is a value using this unit, and y is the corresponding value using the base unit. The elements a and d are optional, and if values are not provided, those parameters are considered to be zero. If values are not provided for both a and d, the formula is equivalent to a fraction with numerator and denominator parameters.
    """
    factor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    formula: Optional[FormulaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    exponent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CatalogSymbol(CodeType):
    """The catalogSymbol is the preferred lexical symbol used for this unit of
    measure.

    The codeSpace attribute in gml:CodeType identifies a namespace for
    the catalog symbol value, and might reference the external catalog.
    The string value in gml:CodeType contains the value of a symbol that
    should be unique within this catalog namespace. This symbol often
    appears explicitly in the catalog, but it could be a combination of
    symbols using a specified algebra of units.
    """
    class Meta:
        name = "catalogSymbol"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class QuantityType(StringOrRefType):
    """The gml:quantityType property indicates the phenomenon to which the units
    apply.

    This element contains an informal description of the phenomenon or
    type of physical quantity that is measured or observed. When the
    physical quantity is the result of an observation or measurement,
    this term is known as observable type or measurand. The use of
    gml:quantityType for references to remote values is deprecated.
    """
    class Meta:
        name = "quantityType"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class QuantityTypeReference(ReferenceType):
    """The gml:quantityTypeReference property indicates the phenomenon to which the
    units apply.

    The content is a reference to a remote value.
    """
    class Meta:
        name = "quantityTypeReference"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UnitOfMeasure(UnitOfMeasureType):
    """The element gml:unitOfMeasure is a property element to refer to a unit of
    measure.

    This is an empty element which carries a reference to a unit of
    measure definition.
    """
    class Meta:
        name = "unitOfMeasure"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UnitDefinitionType(DefinitionType):
    quantity_type: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    quantity_type_reference: Optional[QuantityTypeReference] = field(
        default=None,
        metadata={
            "name": "quantityTypeReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    catalog_symbol: Optional[CatalogSymbol] = field(
        default=None,
        metadata={
            "name": "catalogSymbol",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class ConversionToPreferredUnit(ConversionToPreferredUnitType):
    """The elements gml:conversionToPreferredUnit and
    gml:roughConversionToPreferredUnit represent parameters used to convert
    conventional units to preferred units for this physical quantity type.

    A preferred unit is either a Base Unit or a Derived Unit that is
    selected for all values of one physical quantity type.
    """
    class Meta:
        name = "conversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivationUnitTerm(DerivationUnitTermType):
    """A set of gml:derivationUnitTerm elements describes a derived unit of
    measure.

    Each element carries an integer exponent.  The terms are combined by
    raising each referenced unit to the power of its exponent and
    forming the product. This unit term references another unit of
    measure (uom) and provides an integer exponent applied to that unit
    in defining the compound unit. The exponent may be positive or
    negative, but not zero.
    """
    class Meta:
        name = "derivationUnitTerm"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RoughConversionToPreferredUnit(ConversionToPreferredUnitType):
    """The elements gml:conversionToPreferredUnit and
    gml:roughConversionToPreferredUnit represent parameters used to convert
    conventional units to preferred units for this physical quantity type.

    A preferred unit is either a Base Unit or a Derived Unit that is
    selected for all values of one physical quantity type.
    """
    class Meta:
        name = "roughConversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseUnitType(UnitDefinitionType):
    units_system: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    conversion_to_preferred_unit: Optional[ConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    rough_conversion_to_preferred_unit: Optional[RoughConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DerivedUnitType(UnitDefinitionType):
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )


@dataclass
class UnitDefinition(UnitDefinitionType):
    """A gml:UnitDefinition is a general definition of a unit of measure.

    This generic element is used only for units for which no
    relationship with other units or units systems is known. The content
    model of gml:UnitDefinition adds three additional properties to
    gml:Definition, gml:quantityType, gml:quantityTypeReference and
    gml:catalogSymbol. The gml:catalogSymbol property optionally gives
    the short symbol used for this unit. This element is usually used
    when the relationship of this unit to other units or units systems
    is unknown.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseUnit(BaseUnitType):
    """A base unit is a unit of measure that cannot be derived by combination of
    other base units within a particular system of units.

    For example, in the SI system of units, the base units are metre,
    kilogram, second, Ampere, Kelvin, mole, and candela, for the
    physical quantity types length, mass, time interval, electric
    current, thermodynamic temperature, amount of substance and luminous
    intensity, respectively. gml:BaseUnit extends generic
    gml:UnitDefinition with the property gml:unitsSystem, which carries
    a reference to the units system to which this base unit is asserted
    to belong.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ConventionalUnit(ConventionalUnitType):
    """Conventional units that are neither base units nor defined by direct
    combination of base units are used in many application domains.

    For example electronVolt for energy, feet and nautical miles for
    length.  In most cases there is a known, usually linear, conversion
    to a preferred unit which is either a base unit or derived by direct
    combination of base units. The gml:ConventionalUnit extends
    gml:UnitDefinition with a property that describes a conversion to a
    preferred unit for this physical quantity.  When the conversion is
    exact, the element gml:conversionToPreferredUnit should be used, or
    when the conversion is not exact the element
    gml:roughConversionToPreferredUnit is available. Both of these
    elements have the same content model.  The gml:derivationUnitTerm
    property defined above is included to allow a user to optionally
    record how this unit may be derived from other ("more primitive")
    units.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedUnit(DerivedUnitType):
    """Derived units are defined by combination of other units.

    Derived units are used for quantities other than those corresponding
    to the base units, such as hertz (s-1) for frequency, Newton
    (kg.m/s2) for force.  Derived units based directly on base units are
    usually preferred for quantities other than the fundamental
    quantities within a system. If a derived unit is not the preferred
    unit, the gml:ConventionalUnit element should be used instead. The
    gml:DerivedUnit extends gml:UnitDefinition with the property
    gml:derivationUnitTerms.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
