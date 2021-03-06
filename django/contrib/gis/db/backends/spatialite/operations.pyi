# Stubs for django.contrib.gis.db.backends.spatialite.operations (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.gis.db.backends.base.operations import BaseSpatialOperations
from django.db.backends.sqlite3.operations import DatabaseOperations

class SpatiaLiteOperations(BaseSpatialOperations, DatabaseOperations):
    name = ...  # type: str
    spatialite = ...  # type: bool
    version_regex = ...  # type: Any
    Adapter = ...  # type: Any
    Adaptor = ...  # type: Any
    area = ...  # type: str
    centroid = ...  # type: str
    collect = ...  # type: str
    contained = ...  # type: str
    difference = ...  # type: str
    distance = ...  # type: str
    envelope = ...  # type: str
    extent = ...  # type: str
    intersection = ...  # type: str
    length = ...  # type: str
    num_geom = ...  # type: str
    num_points = ...  # type: str
    point_on_surface = ...  # type: str
    scale = ...  # type: str
    svg = ...  # type: str
    sym_difference = ...  # type: str
    transform = ...  # type: str
    translate = ...  # type: str
    union = ...  # type: str
    unionagg = ...  # type: str
    from_text = ...  # type: str
    from_wkb = ...  # type: str
    select = ...  # type: str
    gis_operators = ...  # type: Any
    def function_names(self): ...
    def unsupported_functions(self): ...
    def spatial_version(self): ...
    def disallowed_aggregates(self): ...
    def gml(self): ...
    def kml(self): ...
    def geojson(self): ...
    def convert_extent(self, box, srid): ...
    def convert_geom(self, wkt, geo_field): ...
    def geo_db_type(self, f): ...
    def get_distance(self, f, value, lookup_type): ...
    def get_geom_placeholder(self, f, value, compiler): ...
    def geos_version(self): ...
    def proj4_version(self): ...
    def spatialite_version(self): ...
    def spatialite_version_tuple(self): ...
    def spatial_aggregate_name(self, agg_name): ...
    def geometry_columns(self): ...
    def spatial_ref_sys(self): ...
    def get_db_converters(self, expression): ...
    def convert_geometry(self, value, expression, connection, context): ...
