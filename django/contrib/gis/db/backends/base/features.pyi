# Stubs for django.contrib.gis.db.backends.base.features (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BaseSpatialFeatures:
    gis_enabled = ...  # type: bool
    has_spatialrefsys_table = ...  # type: bool
    supports_add_srs_entry = ...  # type: bool
    supports_geometry_field_introspection = ...  # type: bool
    supports_3d_storage = ...  # type: bool
    supports_3d_functions = ...  # type: bool
    supports_transform = ...  # type: bool
    supports_real_shape_operations = ...  # type: bool
    supports_null_geometries = ...  # type: bool
    supports_distance_geodetic = ...  # type: bool
    supports_length_geodetic = ...  # type: bool
    supports_num_points_poly = ...  # type: bool
    supports_distances_lookups = ...  # type: bool
    supports_left_right_lookups = ...  # type: bool
    supports_raster = ...  # type: bool
    supports_geometry_field_unique_index = ...  # type: bool
    @property
    def supports_bbcontains_lookup(self): ...
    @property
    def supports_contained_lookup(self): ...
    @property
    def supports_crosses_lookup(self): ...
    @property
    def supports_dwithin_lookup(self): ...
    @property
    def supports_relate_lookup(self): ...
    geoqueryset_methods = ...  # type: Any
    @property
    def supports_collect_aggr(self): ...
    @property
    def supports_extent_aggr(self): ...
    @property
    def supports_make_line_aggr(self): ...
    def __init__(self, *args) -> None: ...
    def __getattr__(self, name): ...
    def has_ops_method(self, method): ...
