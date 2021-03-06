# Stubs for django.contrib.gis.db.models.functions (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.contrib.gis.measure import Area as AreaMeasure, Distance as DistanceMeasure
from django.db.models.expressions import Func, Value

NUMERIC_TYPES = ...  # type: Any

class GeoFunc(Func):
    function = ...  # type: Any
    output_field_class = ...  # type: Any
    geom_param_pos = ...  # type: int
    def __init__(self, *expressions, **extra) -> None: ...
    @property
    def name(self): ...
    @property
    def srid(self): ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, *args, **kwargs): ...

class GeomValue(Value):
    geography = ...  # type: bool
    @property
    def srid(self): ...
    value = ...  # type: Any
    def as_sql(self, compiler, connection): ...
    def as_mysql(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...

class GeoFuncWithGeoParam(GeoFunc):
    def __init__(self, expression, geom, *expressions, **extra) -> None: ...

class SQLiteDecimalToFloatMixin:
    def as_sqlite(self, compiler, connection): ...

class OracleToleranceMixin:
    tolerance = ...  # type: float
    template = ...  # type: Any
    def as_oracle(self, compiler, connection): ...

class Area(OracleToleranceMixin, GeoFunc):
    output_field = ...  # type: Any
    def as_sql(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...

class AsGeoJSON(GeoFunc):
    output_field_class = ...  # type: Any
    def __init__(self, expression, bbox: bool = ..., crs: bool = ..., precision: int = ..., **extra) -> None: ...

class AsGML(GeoFunc):
    geom_param_pos = ...  # type: int
    output_field_class = ...  # type: Any
    def __init__(self, expression, version: int = ..., precision: int = ..., **extra) -> None: ...

class AsKML(AsGML):
    def as_sqlite(self, compiler, connection): ...

class AsSVG(GeoFunc):
    output_field_class = ...  # type: Any
    def __init__(self, expression, relative: bool = ..., precision: int = ..., **extra) -> None: ...

class BoundingCircle(GeoFunc):
    def __init__(self, expression, num_seg: int = ..., **extra) -> None: ...

class Centroid(OracleToleranceMixin, GeoFunc): ...
class Difference(OracleToleranceMixin, GeoFuncWithGeoParam): ...

class DistanceResultMixin:
    def convert_value(self, value, expression, connection, context): ...

class Distance(DistanceResultMixin, OracleToleranceMixin, GeoFuncWithGeoParam):
    output_field_class = ...  # type: Any
    spheroid = ...  # type: Any
    def __init__(self, expr1, expr2, spheroid: Optional[Any] = ..., **extra) -> None: ...
    function = ...  # type: str
    def as_postgresql(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...

class Envelope(GeoFunc): ...
class ForceRHR(GeoFunc): ...

class GeoHash(GeoFunc):
    output_field_class = ...  # type: Any
    def __init__(self, expression, precision: Optional[Any] = ..., **extra) -> None: ...

class Intersection(OracleToleranceMixin, GeoFuncWithGeoParam): ...

class Length(DistanceResultMixin, OracleToleranceMixin, GeoFunc):
    output_field_class = ...  # type: Any
    spheroid = ...  # type: Any
    def __init__(self, expr1, spheroid: bool = ..., **extra) -> None: ...
    def as_sql(self, compiler, connection): ...
    function = ...  # type: str
    def as_postgresql(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection): ...

class MemSize(GeoFunc):
    output_field_class = ...  # type: Any

class NumGeometries(GeoFunc):
    output_field_class = ...  # type: Any

class NumPoints(GeoFunc):
    output_field_class = ...  # type: Any
    def as_sqlite(self, compiler, connection): ...

class Perimeter(DistanceResultMixin, OracleToleranceMixin, GeoFunc):
    output_field_class = ...  # type: Any
    function = ...  # type: Any
    def as_postgresql(self, compiler, connection): ...

class PointOnSurface(OracleToleranceMixin, GeoFunc): ...
class Reverse(GeoFunc): ...

class Scale(SQLiteDecimalToFloatMixin, GeoFunc):
    def __init__(self, expression, x, y, z: float = ..., **extra) -> None: ...

class SnapToGrid(SQLiteDecimalToFloatMixin, GeoFunc):
    def __init__(self, expression, *args, **extra) -> None: ...

class SymDifference(OracleToleranceMixin, GeoFuncWithGeoParam): ...

class Transform(GeoFunc):
    def __init__(self, expression, srid, **extra) -> None: ...
    @property
    def srid(self): ...
    def convert_value(self, value, expression, connection, context): ...

class Translate(Scale):
    def as_sqlite(self, compiler, connection): ...

class Union(OracleToleranceMixin, GeoFuncWithGeoParam): ...
