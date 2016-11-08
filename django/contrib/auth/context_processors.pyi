# Stubs for django.contrib.auth.context_processors (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PermLookupDict:
    def __init__(self, user, app_label) -> None: ...
    def __getitem__(self, perm_name): ...
    def __iter__(self): ...
    def __bool__(self): ...
    def __nonzero__(self): ...

class PermWrapper:
    user = ...  # type: Any
    def __init__(self, user) -> None: ...
    def __getitem__(self, app_label): ...
    def __iter__(self): ...
    def __contains__(self, perm_name): ...

def auth(request): ...
