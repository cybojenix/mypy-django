# Stubs for django.contrib.gis.db.backends.postgis.features (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.gis.db.backends.base.features import BaseSpatialFeatures
from django.db.backends.postgresql.features import DatabaseFeatures as Psycopg2DatabaseFeatures

class DatabaseFeatures(BaseSpatialFeatures, Psycopg2DatabaseFeatures):
    supports_3d_storage = ...  # type: bool
    supports_3d_functions = ...  # type: bool
    supports_left_right_lookups = ...  # type: bool
    supports_raster = ...  # type: bool