# Stubs for django.template.loader (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import base
from .backends.django import DjangoTemplates as DjangoTemplates
from .base import Origin as Origin
from .engine import _context_instance_undefined as _context_instance_undefined, _dictionary_undefined as _dictionary_undefined, _dirs_undefined as _dirs_undefined
from .exceptions import TemplateDoesNotExist as TemplateDoesNotExist
from .loaders import base as base

def get_template(template_name, dirs: Any = ..., using: Optional[Any] = ...): ...
def select_template(template_name_list, dirs: Any = ..., using: Optional[Any] = ...): ...
def render_to_string(template_name, context: Optional[Any] = ..., context_instance: Any = ..., dirs: Any = ..., dictionary: Any = ..., request: Optional[Any] = ..., using: Optional[Any] = ...): ...

class BaseLoader(base.Loader):
    def __init__(self, *args, **kwargs) -> None: ...

class LoaderOrigin:
    alternative = ...  # type: str
    deprecation_warning = ...  # type: Any