# Stubs for django.template.response (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.http import HttpResponse
from .backends.django import DjangoTemplates as DjangoTemplates
from .backends.django import Template as BackendTemplate
from .base import Template as Template
from .context import Context as Context, RequestContext as RequestContext, _current_app_undefined as _current_app_undefined
from .loader import get_template as get_template, select_template as select_template

class ContentNotRenderedError(Exception): ...

class SimpleTemplateResponse(HttpResponse):
    rendering_attrs = ...  # type: Any
    template_name = ...  # type: Any
    context_data = ...  # type: Any
    using = ...  # type: Any
    def __init__(self, template, context: Optional[Any] = ..., content_type: Optional[Any] = ..., status: Optional[Any] = ..., charset: Optional[Any] = ..., using: Optional[Any] = ...) -> None: ...
    def resolve_template(self, template): ...
    def resolve_context(self, context): ...
    @property
    def rendered_content(self): ...
    def add_post_render_callback(self, callback): ...
    content = ...  # type: Any
    def render(self): ...
    @property
    def is_rendered(self): ...
    def __iter__(self): ...
    @property
    def content(self): ...
    @content.setter
    def content(self, value): ...

class TemplateResponse(SimpleTemplateResponse):
    rendering_attrs = ...  # type: Any
    def __init__(self, request, template, context: Optional[Any] = ..., content_type: Optional[Any] = ..., status: Optional[Any] = ..., current_app: Any = ..., charset: Optional[Any] = ..., using: Optional[Any] = ...) -> None: ...