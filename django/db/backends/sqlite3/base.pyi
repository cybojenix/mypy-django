# Stubs for django.db.backends.sqlite3.base (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import Database
from django.db.backends import utils as backend_utils
from django.db.backends.base.base import BaseDatabaseWrapper
from pysqlite2 import dbapi2 as Database
from sqlite3 import dbapi2 as Database
from .client import DatabaseClient as DatabaseClient
from .creation import DatabaseCreation as DatabaseCreation
from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import DatabaseIntrospection as DatabaseIntrospection
from .operations import DatabaseOperations as DatabaseOperations
from .schema import DatabaseSchemaEditor as DatabaseSchemaEditor

pytz = ...  # type: Any
DatabaseError = ...  # type: Any
IntegrityError = ...  # type: Any

def adapt_datetime_warn_on_aware_datetime(value): ...
def decoder(conv_func): ...

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = ...  # type: str
    data_types = ...  # type: Any
    data_types_suffix = ...  # type: Any
    operators = ...  # type: Any
    pattern_esc = ...  # type: str
    pattern_ops = ...  # type: Any
    Database = ...  # type: Any
    SchemaEditorClass = ...  # type: Any
    features = ...  # type: Any
    ops = ...  # type: Any
    client = ...  # type: Any
    creation = ...  # type: Any
    introspection = ...  # type: Any
    validation = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def get_connection_params(self): ...
    def get_new_connection(self, conn_params): ...
    def init_connection_state(self): ...
    def create_cursor(self): ...
    def close(self): ...
    def check_constraints(self, table_names: Optional[Any] = ...): ...
    def is_usable(self): ...
    def is_in_memory_db(self, name): ...

FORMAT_QMARK_REGEX = ...  # type: Any

class SQLiteCursorWrapper(Database.Cursor):
    def execute(self, query, params: Optional[Any] = ...): ...
    def executemany(self, query, param_list): ...
    def convert_query(self, query): ...
