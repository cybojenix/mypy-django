# Stubs for django.contrib.sessions.backends.cache (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.contrib.sessions.backends.base import SessionBase

KEY_PREFIX = ...  # type: str

class SessionStore(SessionBase):
    cache_key_prefix = ...  # type: Any
    def __init__(self, session_key: Optional[Any] = ...) -> None: ...
    @property
    def cache_key(self): ...
    def load(self): ...
    modified = ...  # type: bool
    def create(self): ...
    def save(self, must_create: bool = ...): ...
    def exists(self, session_key): ...
    def delete(self, session_key: Optional[Any] = ...): ...
    @classmethod
    def clear_expired(cls): ...
