# Stubs for django.utils.text (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.functional import SimpleLazyObject
from django.utils.translation import ugettext as _

capfirst = ...  # type: Any
re_words = ...  # type: Any
re_chars = ...  # type: Any
re_tag = ...  # type: Any
re_newlines = ...  # type: Any
re_camel_case = ...  # type: Any

def wrap(text, width): ...

wrap = ...  # type: Any

class Truncator(SimpleLazyObject):
    def __init__(self, text) -> None: ...
    def add_truncation_text(self, text, truncate: Optional[Any] = ...): ...
    def chars(self, num, truncate: Optional[Any] = ..., html: bool = ...): ...
    chars = ...  # type: Any
    def words(self, num, truncate: Optional[Any] = ..., html: bool = ...): ...
    words = ...  # type: Any

def get_valid_filename(s): ...

get_valid_filename = ...  # type: Any

def get_text_list(list_, last_word: Any = ...): ...

get_text_list = ...  # type: Any

def normalize_newlines(text): ...

normalize_newlines = ...  # type: Any

def phone2numeric(phone): ...

phone2numeric = ...  # type: Any

def compress_string(s): ...

class StreamingBuffer:
    vals = ...  # type: Any
    def __init__(self) -> None: ...
    def write(self, val): ...
    def read(self): ...
    def flush(self): ...
    def close(self): ...

def compress_sequence(sequence): ...

smart_split_re = ...  # type: Any

def smart_split(text): ...
def unescape_entities(text): ...

unescape_entities = ...  # type: Any

def unescape_string_literal(s): ...

unescape_string_literal = ...  # type: Any

def slugify(value, allow_unicode: bool = ...): ...

slugify = ...  # type: Any

def camel_case_to_spaces(value): ...
