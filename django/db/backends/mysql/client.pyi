# Stubs for django.db.backends.mysql.client (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.client import BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name = ...  # type: str
    @classmethod
    def settings_to_cmd_args(cls, settings_dict): ...
    def runshell(self): ...
