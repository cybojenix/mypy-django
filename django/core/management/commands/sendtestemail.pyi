# Stubs for django.core.management.commands.sendtestemail (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    missing_args_message = ...  # type: str
    def add_arguments(self, parser): ...
    def handle(self, *args, **kwargs): ...