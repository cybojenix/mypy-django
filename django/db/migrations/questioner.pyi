# Stubs for django.db.migrations.questioner (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .loader import MigrationLoader as MigrationLoader

class MigrationQuestioner:
    defaults = ...  # type: Any
    specified_apps = ...  # type: Any
    dry_run = ...  # type: Any
    def __init__(self, defaults: Optional[Any] = ..., specified_apps: Optional[Any] = ..., dry_run: Optional[Any] = ...) -> None: ...
    def ask_initial(self, app_label): ...
    def ask_not_null_addition(self, field_name, model_name): ...
    def ask_not_null_alteration(self, field_name, model_name): ...
    def ask_rename(self, model_name, old_name, new_name, field_instance): ...
    def ask_rename_model(self, old_model_state, new_model_state): ...
    def ask_merge(self, app_label): ...

class InteractiveMigrationQuestioner(MigrationQuestioner):
    def ask_not_null_addition(self, field_name, model_name): ...
    def ask_not_null_alteration(self, field_name, model_name): ...
    def ask_rename(self, model_name, old_name, new_name, field_instance): ...
    def ask_rename_model(self, old_model_state, new_model_state): ...
    def ask_merge(self, app_label): ...

class NonInteractiveMigrationQuestioner(MigrationQuestioner):
    def ask_not_null_addition(self, field_name, model_name): ...
    def ask_not_null_alteration(self, field_name, model_name): ...
