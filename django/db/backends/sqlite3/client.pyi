# Stubs for django.db.backends.sqlite3.client (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.client import BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name = ...  # type: str
    def runshell(self): ...
