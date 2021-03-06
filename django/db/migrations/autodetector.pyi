# Stubs for django.db.migrations.autodetector (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .topological_sort import stable_topological_sort as stable_topological_sort

class MigrationAutodetector:
    from_state = ...  # type: Any
    to_state = ...  # type: Any
    questioner = ...  # type: Any
    existing_apps = ...  # type: Any
    def __init__(self, from_state, to_state, questioner: Optional[Any] = ...) -> None: ...
    def changes(self, graph, trim_to_apps: Optional[Any] = ..., convert_apps: Optional[Any] = ..., migration_name: Optional[Any] = ...): ...
    def deep_deconstruct(self, obj): ...
    def only_relation_agnostic_fields(self, fields): ...
    def check_dependency(self, operation, dependency): ...
    def add_operation(self, app_label, operation, dependencies: Optional[Any] = ..., beginning: bool = ...): ...
    def swappable_first_key(self, item): ...
    renamed_models = ...  # type: Any
    renamed_models_rel = ...  # type: Any
    def generate_renamed_models(self): ...
    def generate_created_models(self): ...
    def generate_created_proxies(self): ...
    def generate_deleted_models(self): ...
    def generate_deleted_proxies(self): ...
    renamed_fields = ...  # type: Any
    def generate_renamed_fields(self): ...
    def generate_added_fields(self): ...
    def generate_removed_fields(self): ...
    def generate_altered_fields(self): ...
    def generate_altered_unique_together(self): ...
    def generate_altered_index_together(self): ...
    def generate_altered_db_table(self): ...
    def generate_altered_options(self): ...
    def generate_altered_order_with_respect_to(self): ...
    def generate_altered_managers(self): ...
    def arrange_for_graph(self, changes, graph, migration_name: Optional[Any] = ...): ...
    @classmethod
    def suggest_name(cls, ops): ...
    @classmethod
    def parse_number(cls, name): ...
