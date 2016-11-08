# Stubs for django.contrib.messages.storage.base (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

LEVEL_TAGS = ...  # type: Any

class Message:
    level = ...  # type: Any
    message = ...  # type: Any
    extra_tags = ...  # type: Any
    def __init__(self, level, message, extra_tags: Optional[Any] = ...) -> None: ...
    def __eq__(self, other): ...
    tags = ...  # type: Any
    @property
    def level_tag(self): ...

class BaseStorage:
    request = ...  # type: Any
    used = ...  # type: bool
    added_new = ...  # type: bool
    def __init__(self, request, *args, **kwargs) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, item): ...
    def update(self, response): ...
    def add(self, level, message, extra_tags: str = ...): ...
    level = ...  # type: Any
