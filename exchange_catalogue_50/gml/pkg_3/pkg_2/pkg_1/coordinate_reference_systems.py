from dataclasses import dataclass, field
from typing import List, Optional, Union
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.basic_types import (
    CodeWithAuthorityType,
    NilReasonEnumerationValue,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coordinate_operations import GeneralConversionPropertyType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.coordinate_systems import (
    AffineCspropertyType,
    CartesianCspropertyType,
    CoordinateSystemPropertyType,
    CylindricalCspropertyType,
    EllipsoidalCspropertyType,
    LinearCspropertyType,
    PolarCspropertyType,
    SphericalCspropertyType,
    TimeCspropertyType,
    UserDefinedCspropertyType,
    VerticalCspropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.datums import (
    EngineeringDatumPropertyType,
    GeodeticDatumPropertyType,
    ImageDatumPropertyType,
    TemporalDatumPropertyType,
    VerticalDatumPropertyType,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.deprecated_types import (
    BaseGeographicCrs,
    DefinedByConversion,
    IncludesSingleCrs,
    UsesAffineCs,
    UsesCs,
    UsesCartesianCs,
    UsesEllipsoidalCs,
    UsesEngineeringDatum,
    UsesGeodeticDatum,
    UsesImageDatum,
    UsesObliqueCartesianCs,
    UsesSphericalCs,
    UsesTemporalCs,
    UsesTemporalDatum,
    UsesTimeCs,
    UsesVerticalCs,
    UsesVerticalDatum,
)
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.gml_base import AggregationType
from exchange_catalogue_50.gml.pkg_3.pkg_2.pkg_1.reference_systems import AbstractCrstype
from exchange_catalogue_50.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticCrspropertyType:
    """
    Gml:GeodeticCRSPropertyType is a property type for association roles to a
    geodetic coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "GeodeticCRSPropertyType"

    geodetic_crs: Optional["GeodeticCrs"] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class SingleCrspropertyType:
    """
    Gml:SingleCRSPropertyType is a property type for association roles to a single
    coordinate reference system, either referencing or containing the definition of
    that coordinate reference system.
    """
    class Meta:
        name = "SingleCRSPropertyType"

    geocentric_crs: Optional["GeocentricCrs"] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geographic_crs: Optional["GeographicCrs"] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    temporal_crs: Optional["TemporalCrs"] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    image_crs: Optional["ImageCrs"] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    engineering_crs: Optional["EngineeringCrs"] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_crs: Optional["VerticalCrs"] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_crs: Optional["GeodeticCrs"] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    derived_crs: Optional["DerivedCrs"] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    projected_crs: Optional["ProjectedCrs"] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class AffineCs2(AffineCspropertyType):
    """
    Gml:affineCS is an association role to the affine coordinate system used by
    this CRS.
    """
    class Meta:
        name = "affineCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CartesianCs2(CartesianCspropertyType):
    """
    Gml:cartesianCS is an association role to the Cartesian coordinate system used
    by this CRS.
    """
    class Meta:
        name = "cartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Conversion2(GeneralConversionPropertyType):
    """
    Gml:conversion is an association role to the coordinate conversion used to
    define the derived CRS.
    """
    class Meta:
        name = "conversion"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystem(CoordinateSystemPropertyType):
    """
    An association role to the coordinate system used by this CRS.
    """
    class Meta:
        name = "coordinateSystem"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCs2(CylindricalCspropertyType):
    """
    Gml:cylindricalCS is an association role to the cylindrical coordinate system
    used by this CRS.
    """
    class Meta:
        name = "cylindricalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrstype(CodeWithAuthorityType):
    """The gml:derivedCRSType property describes the type of a derived coordinate
    reference system.

    The required codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """
    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidalCs2(EllipsoidalCspropertyType):
    """
    Gml:ellipsoidalCS is an association role to the ellipsoidal coordinate system
    used by this CRS.
    """
    class Meta:
        name = "ellipsoidalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringDatum2(EngineeringDatumPropertyType):
    """
    Gml:engineeringDatum is an association role to the engineering datum used by
    this CRS.
    """
    class Meta:
        name = "engineeringDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatum2(GeodeticDatumPropertyType):
    """
    Gml:geodeticDatum is an association role to the geodetic datum used by this
    CRS.
    """
    class Meta:
        name = "geodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatum2(ImageDatumPropertyType):
    """
    Gml:imageDatum is an association role to the image datum used by this CRS.
    """
    class Meta:
        name = "imageDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearCs2(LinearCspropertyType):
    """
    Gml:linearCS is an association role to the linear coordinate system used by
    this CRS.
    """
    class Meta:
        name = "linearCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolarCs2(PolarCspropertyType):
    """
    Gml:polarCS is an association role to the polar coordinate system used by this
    CRS.
    """
    class Meta:
        name = "polarCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SphericalCs2(SphericalCspropertyType):
    """
    Gml:sphericalCS is an association role to the spherical coordinate system used
    by this CRS.
    """
    class Meta:
        name = "sphericalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalDatum2(TemporalDatumPropertyType):
    """
    Gml:temporalDatum is an association role to the temporal datum used by this
    CRS.
    """
    class Meta:
        name = "temporalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCs2(TimeCspropertyType):
    """
    Gml:timeCS is an association role to the time coordinate system used by this
    CRS.
    """
    class Meta:
        name = "timeCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCs2(UserDefinedCspropertyType):
    """
    Gml:userDefinedCS is an association role to the user defined coordinate system
    used by this CRS.
    """
    class Meta:
        name = "userDefinedCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCs2(VerticalCspropertyType):
    """
    Gml:verticalCS is an association role to the vertical coordinate system used by
    this CRS.
    """
    class Meta:
        name = "verticalCS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatum2(VerticalDatumPropertyType):
    """
    Gml:verticalDatum is an association role to the vertical datum used by this
    CRS.
    """
    class Meta:
        name = "verticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralDerivedCrstype(AbstractCrstype):
    class Meta:
        name = "AbstractGeneralDerivedCRSType"

    defined_by_conversion: Optional[DefinedByConversion] = field(
        default=None,
        metadata={
            "name": "definedByConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    conversion: Optional[Conversion2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class EngineeringCrstype(AbstractCrstype):
    class Meta:
        name = "EngineeringCRSType"

    uses_affine_cs: Optional[UsesAffineCs] = field(
        default=None,
        metadata={
            "name": "usesAffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    affine_cs: Optional[AffineCs2] = field(
        default=None,
        metadata={
            "name": "affineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cylindrical_cs: Optional[CylindricalCs2] = field(
        default=None,
        metadata={
            "name": "cylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    linear_cs: Optional[LinearCs2] = field(
        default=None,
        metadata={
            "name": "linearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polar_cs: Optional[PolarCs2] = field(
        default=None,
        metadata={
            "name": "polarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    user_defined_cs: Optional[UserDefinedCs2] = field(
        default=None,
        metadata={
            "name": "userDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_engineering_datum: Optional[UsesEngineeringDatum] = field(
        default=None,
        metadata={
            "name": "usesEngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    engineering_datum: Optional[EngineeringDatum2] = field(
        default=None,
        metadata={
            "name": "engineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class GeodeticCrstype(AbstractCrstype):
    """
    Gml:GeodeticCRS is a coordinate reference system based on a geodetic datum.
    """
    class Meta:
        name = "GeodeticCRSType"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    ellipsoidal_cs: Optional[EllipsoidalCs2] = field(
        default=None,
        metadata={
            "name": "ellipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_datum: Optional[GeodeticDatum2] = field(
        default=None,
        metadata={
            "name": "geodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class ImageCrstype(AbstractCrstype):
    class Meta:
        name = "ImageCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_affine_cs: Optional[UsesAffineCs] = field(
        default=None,
        metadata={
            "name": "usesAffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    affine_cs: Optional[AffineCs2] = field(
        default=None,
        metadata={
            "name": "affineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_oblique_cartesian_cs: Optional[UsesObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    image_datum: Optional[ImageDatum2] = field(
        default=None,
        metadata={
            "name": "imageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TemporalCrstype(AbstractCrstype):
    class Meta:
        name = "TemporalCRSType"

    uses_time_cs: Optional[UsesTimeCs] = field(
        default=None,
        metadata={
            "name": "usesTimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    time_cs: Optional[TimeCs2] = field(
        default=None,
        metadata={
            "name": "timeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_temporal_cs: Optional[UsesTemporalCs] = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_temporal_datum: Optional[UsesTemporalDatum] = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    temporal_datum: Optional[TemporalDatum2] = field(
        default=None,
        metadata={
            "name": "temporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class VerticalCrstype(AbstractCrstype):
    class Meta:
        name = "VerticalCRSType"

    uses_vertical_cs: Optional[UsesVerticalCs] = field(
        default=None,
        metadata={
            "name": "usesVerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_cs: Optional[VerticalCs2] = field(
        default=None,
        metadata={
            "name": "verticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_vertical_datum: Optional[UsesVerticalDatum] = field(
        default=None,
        metadata={
            "name": "usesVerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    vertical_datum: Optional[VerticalDatum2] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class BaseCrs(SingleCrspropertyType):
    """
    Gml:baseCRS is an association role to the coordinate reference system used by
    this derived CRS.
    """
    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseGeodeticCrs(GeodeticCrspropertyType):
    """
    Gml:baseGeodeticCRS is an association role to the geodetic coordinate reference
    system used by this projected CRS.
    """
    class Meta:
        name = "baseGeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ComponentReferenceSystem(SingleCrspropertyType):
    """The gml:componentReferenceSystem elements are an ordered sequence of
    associations to all the component coordinate reference systems included in this
    compound coordinate reference system.

    The gml:AggregationAttributeGroup should be used to specify that the
    gml:componentReferenceSystem properties are ordered.
    """
    class Meta:
        name = "componentReferenceSystem"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompoundCrstype(AbstractCrstype):
    class Meta:
        name = "CompoundCRSType"

    includes_single_crs: List[IncludesSingleCrs] = field(
        default_factory=list,
        metadata={
            "name": "includesSingleCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    component_reference_system: List[ComponentReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "componentReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class DerivedCrstype1(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "DerivedCRSType"

    base_crs: Optional[BaseCrs] = field(
        default=None,
        metadata={
            "name": "baseCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    derived_crstype: Optional[DerivedCrstype] = field(
        default=None,
        metadata={
            "name": "derivedCRSType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class EngineeringCrs(EngineeringCrstype):
    """Gml:EngineeringCRS is a contextually local coordinate reference system which
    can be divided into two broad categories:

    -       earth-fixed systems applied to engineering activities on or near the surface of the earth;
    -       CRSs on moving platforms such as road vehicles, vessels, aircraft, or spacecraft, see ISO 19111 8.3.
    """
    class Meta:
        name = "EngineeringCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticCrs(GeodeticCrstype):
    class Meta:
        name = "GeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageCrs(ImageCrstype):
    """Gml:ImageCRS is an engineering coordinate reference system applied to
    locations in images.

    Image coordinate reference systems are treated as a separate sub-
    type because the definition of the associated image datum contains
    two attributes not relevant to other engineering datums.
    """
    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "ProjectedCRSType"

    base_geodetic_crs: Optional[BaseGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "baseGeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    base_geographic_crs: Optional[BaseGeographicCrs] = field(
        default=None,
        metadata={
            "name": "baseGeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class TemporalCrs(TemporalCrstype):
    """
    Gml:TemporalCRS is a 1D coordinate reference system used for the recording of
    time.
    """
    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCrs(VerticalCrstype):
    """Gml:VerticalCRS is a 1D coordinate reference system used for recording
    heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompoundCrs(CompoundCrstype):
    """Gml:CompundCRS is a coordinate reference system describing the position of
    points through two or more independent coordinate reference systems.

    It is associated with a non-repeating sequence of two or more
    instances of SingleCRS.
    """
    class Meta:
        name = "CompoundCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrs(DerivedCrstype1):
    """Gml:DerivedCRS is a single coordinate reference system that is defined by
    its coordinate conversion from another single coordinate reference system known
    as the base CRS.

    The base CRS can be a projected coordinate reference system, if this
    DerivedCRS is used for a georectified grid coverage as described in
    ISO 19123, Clause 8.
    """
    class Meta:
        name = "DerivedCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrspropertyType:
    """
    Gml:EngineeringCRSPropertyType is a property type for association roles to an
    engineering coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "EngineeringCRSPropertyType"

    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class ImageCrspropertyType:
    """
    Gml:ImageCRSPropertyType is a property type for association roles to an image
    coordinate reference system, either referencing or containing the definition of
    that reference system.
    """
    class Meta:
        name = "ImageCRSPropertyType"

    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class ProjectedCrs(ProjectedCrstype):
    """Gml:ProjectedCRS is a 2D coordinate reference system used to approximate the
    shape of the earth on a planar surface, but in such a way that the distortion
    that is inherent to the approximation is carefully controlled and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCrspropertyType:
    """
    Gml:TemporalCRSPropertyType is a property type for association roles to a
    temporal coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "TemporalCRSPropertyType"

    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class VerticalCrspropertyType:
    """
    Gml:VerticalCRSPropertyType is a property type for association roles to a
    vertical coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "VerticalCRSPropertyType"

    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class CompoundCrspropertyType:
    """
    Gml:CompoundCRSPropertyType is a property type for association roles to a
    compound coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "CompoundCRSPropertyType"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class DerivedCrspropertyType:
    """
    Gml:DerivedCRSPropertyType is a property type for association roles to a non-
    projected derived coordinate reference system, either referencing or containing
    the definition of that reference system.
    """
    class Meta:
        name = "DerivedCRSPropertyType"

    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class ProjectedCrspropertyType:
    """
    Gml:ProjectedCRSPropertyType is a property type for association roles to a
    projected coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "ProjectedCRSPropertyType"

    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
