# Stubs for django.contrib.messages.storage.session (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.messages.storage.base import BaseStorage

class SessionStorage(BaseStorage):
    session_key = ...  # type: str
    def __init__(self, request, *args, **kwargs) -> None: ...
    def serialize_messages(self, messages): ...
    def deserialize_messages(self, data): ...