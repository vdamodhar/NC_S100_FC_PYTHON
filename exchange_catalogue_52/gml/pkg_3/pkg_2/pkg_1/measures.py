from dataclasses import dataclass
from exchange_catalogue_52.gml.pkg_3.pkg_2.pkg_1.basic_types import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AngleType(MeasureType):
    pass


@dataclass
class AreaType(MeasureType):
    pass


@dataclass
class GridLengthType(MeasureType):
    pass


@dataclass
class LengthType(MeasureType):
    """This is a prototypical definition for a specific measure type defined as a
    vacuous extension (i.e. aliases) of gml:MeasureType.

    In this case, the content model supports the description of a length
    (or distance) quantity, with its units. The unit of measure
    referenced by uom shall be suitable for a length, such as metres or
    feet.
    """


@dataclass
class ScaleType(MeasureType):
    pass


@dataclass
class SpeedType(MeasureType):
    pass


@dataclass
class TimeType(MeasureType):
    pass


@dataclass
class VolumeType(MeasureType):
    pass


@dataclass
class Measure(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """
    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Angle(AngleType):
    """
    The gml:angle property element is used to record the value of an angle quantity
    as a single number, with its units.
    """
    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml/3.2"
