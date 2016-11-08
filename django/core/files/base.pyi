# Stubs for django.core.files.base (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.files.utils import FileProxyMixin

class File(FileProxyMixin):
    DEFAULT_CHUNK_SIZE = ...  # type: Any
    file = ...  # type: Any
    name = ...  # type: Any
    mode = ...  # type: Any
    def __init__(self, file, name: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    def __nonzero__(self): ...
    def __len__(self): ...
    size = ...  # type: Any
    closed = ...  # type: Any
    def chunks(self, chunk_size: Optional[Any] = ...): ...
    def multiple_chunks(self, chunk_size: Optional[Any] = ...): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, tb): ...
    def open(self, mode: Optional[Any] = ...): ...
    def close(self): ...

class ContentFile(File):
    size = ...  # type: Any
    def __init__(self, content, name: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    def __nonzero__(self): ...
    def open(self, mode: Optional[Any] = ...): ...
    def close(self): ...

def endswith_cr(line): ...
def endswith_lf(line): ...
def equals_lf(line): ...
