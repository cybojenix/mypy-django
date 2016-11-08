# Stubs for django.contrib.gis.admin.options (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.admin import ModelAdmin

spherical_mercator_srid = ...  # type: int

class GeoModelAdmin(ModelAdmin):
    default_lon = ...  # type: int
    default_lat = ...  # type: int
    default_zoom = ...  # type: int
    display_wkt = ...  # type: bool
    display_srid = ...  # type: bool
    extra_js = ...  # type: Any
    num_zoom = ...  # type: int
    max_zoom = ...  # type: bool
    min_zoom = ...  # type: bool
    units = ...  # type: bool
    max_resolution = ...  # type: bool
    max_extent = ...  # type: bool
    modifiable = ...  # type: bool
    mouse_position = ...  # type: bool
    scale_text = ...  # type: bool
    layerswitcher = ...  # type: bool
    scrollable = ...  # type: bool
    map_width = ...  # type: int
    map_height = ...  # type: int
    map_srid = ...  # type: int
    map_template = ...  # type: str
    openlayers_url = ...  # type: str
    point_zoom = ...  # type: Any
    wms_url = ...  # type: str
    wms_layer = ...  # type: str
    wms_name = ...  # type: str
    wms_options = ...  # type: Any
    debug = ...  # type: bool
    widget = ...  # type: Any
    @property
    def media(self): ...
    def formfield_for_dbfield(self, db_field, **kwargs): ...
    def get_map_widget(self, db_field): ...

class OSMGeoAdmin(GeoModelAdmin):
    map_template = ...  # type: str
    num_zoom = ...  # type: int
    map_srid = ...  # type: Any
    max_extent = ...  # type: str
    max_resolution = ...  # type: str
    point_zoom = ...  # type: Any
    units = ...  # type: str
    def __init__(self, *args) -> None: ...
