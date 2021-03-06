# Stubs for django.db.backends.sqlite3.schema (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.schema import BaseDatabaseSchemaEditor

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_delete_table = ...  # type: str
    sql_create_inline_fk = ...  # type: str
    sql_create_unique = ...  # type: str
    sql_delete_unique = ...  # type: str
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...
    def quote_value(self, value): ...
    def delete_model(self, model, handle_autom2m: bool = ...): ...
    def add_field(self, model, field): ...
    def remove_field(self, model, field): ...
    def alter_index_together(self, model, old_index_together, new_index_together): ...
    def alter_unique_together(self, model, old_unique_together, new_unique_together): ...
