# Stubs for django.template.loader_tags (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import Node as Node, Template as Template, TemplateSyntaxError as TemplateSyntaxError, TextNode as TextNode, Variable as Variable, token_kwargs as token_kwargs
from .library import Library as Library

register = ...  # type: Any
BLOCK_CONTEXT_KEY = ...  # type: str
logger = ...  # type: Any

class ExtendsError(Exception): ...

class BlockContext:
    blocks = ...  # type: Any
    def __init__(self) -> None: ...
    def add_blocks(self, blocks): ...
    def pop(self, name): ...
    def push(self, name, block): ...
    def get_block(self, name): ...

class BlockNode(Node):
    def __init__(self, name, nodelist, parent: Optional[Any] = ...) -> None: ...
    def render(self, context): ...
    def super(self): ...

class ExtendsNode(Node):
    must_be_first = ...  # type: bool
    context_key = ...  # type: str
    nodelist = ...  # type: Any
    parent_name = ...  # type: Any
    template_dirs = ...  # type: Any
    blocks = ...  # type: Any
    def __init__(self, nodelist, parent_name, template_dirs: Optional[Any] = ...) -> None: ...
    def find_template(self, template_name, context): ...
    def get_parent(self, context): ...
    def render(self, context): ...

class IncludeNode(Node):
    context_key = ...  # type: str
    template = ...  # type: Any
    extra_context = ...  # type: Any
    isolated_context = ...  # type: Any
    def __init__(self, template, *args, **kwargs) -> None: ...
    def render(self, context): ...

def do_block(parser, token): ...
def do_extends(parser, token): ...
def do_include(parser, token): ...
