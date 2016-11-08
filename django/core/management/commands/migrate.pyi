# Stubs for django.core.management.commands.migrate (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    def add_arguments(self, parser): ...
    verbosity = ...  # type: Any
    interactive = ...  # type: Any
    def handle(self, *args, **options): ...
    start = ...  # type: Any
    def migration_progress_callback(self, action, migration: Optional[Any] = ..., fake: bool = ...): ...
    def sync_apps(self, connection, app_labels): ...