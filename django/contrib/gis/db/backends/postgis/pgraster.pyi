# Stubs for django.contrib.gis.db.backends.postgis.pgraster (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .const import GDAL_TO_POSTGIS as GDAL_TO_POSTGIS, GDAL_TO_STRUCT as GDAL_TO_STRUCT, POSTGIS_HEADER_STRUCTURE as POSTGIS_HEADER_STRUCTURE, POSTGIS_TO_GDAL as POSTGIS_TO_GDAL, STRUCT_SIZE as STRUCT_SIZE

def pack(structure, data): ...
def unpack(structure, data): ...
def chunk(data, index): ...
def get_pgraster_srid(data): ...
def from_pgraster(data): ...
def to_pgraster(rast): ...
