# Stubs for django.core.management.commands.sqlmigrate (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    output_transaction = ...  # type: bool
    def add_arguments(self, parser): ...
    def execute(self, *args, **options): ...
    def handle(self, *args, **options): ...
