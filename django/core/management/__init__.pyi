# Stubs for django.core.management (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def find_commands(management_dir): ...
def load_command_class(app_name, name): ...
def get_commands(): ...
def call_command(name, *args, **options): ...

class ManagementUtility:
    argv = ...  # type: Any
    prog_name = ...  # type: Any
    settings_exception = ...  # type: Any
    def __init__(self, argv: Optional[Any] = ...) -> None: ...
    def main_help_text(self, commands_only: bool = ...): ...
    def fetch_command(self, subcommand): ...
    def autocomplete(self): ...
    def execute(self): ...

def execute_from_command_line(argv: Optional[Any] = ...): ...
