# Stubs for django.contrib.auth.management.commands.changepassword (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    requires_system_checks = ...  # type: bool
    def add_arguments(self, parser): ...
    def handle(self, *args, **options): ...
