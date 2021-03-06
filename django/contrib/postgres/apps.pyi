# Stubs for django.contrib.postgres.apps (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .lookups import Unaccent as Unaccent
from .signals import register_hstore_handler as register_hstore_handler

class PostgresConfig(AppConfig):
    name = ...  # type: str
    verbose_name = ...  # type: Any
    def ready(self): ...
