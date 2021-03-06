# Stubs for django.utils.synch (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class RWLock:
    mutex = ...  # type: Any
    can_read = ...  # type: Any
    can_write = ...  # type: Any
    active_readers = ...  # type: int
    active_writers = ...  # type: int
    waiting_readers = ...  # type: int
    waiting_writers = ...  # type: int
    def __init__(self) -> None: ...
    def reader_enters(self): ...
    def reader_leaves(self): ...
    def reader(self): ...
    def writer_enters(self): ...
    def writer_leaves(self): ...
    def writer(self): ...
