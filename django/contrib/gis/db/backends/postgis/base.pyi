# Stubs for django.contrib.gis.db.backends.postgis.base (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.backends.postgresql.base import DatabaseWrapper as Psycopg2DatabaseWrapper
from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import PostGISIntrospection as PostGISIntrospection
from .operations import PostGISOperations as PostGISOperations
from .schema import PostGISSchemaEditor as PostGISSchemaEditor

class DatabaseWrapper(Psycopg2DatabaseWrapper):
    SchemaEditorClass = ...  # type: Any
    features = ...  # type: Any
    ops = ...  # type: Any
    introspection = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def prepare_database(self): ...