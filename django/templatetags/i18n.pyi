# Stubs for django.templatetags.i18n (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.template import Node

register = ...  # type: Any

class GetAvailableLanguagesNode(Node):
    variable = ...  # type: Any
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class GetLanguageInfoNode(Node):
    lang_code = ...  # type: Any
    variable = ...  # type: Any
    def __init__(self, lang_code, variable) -> None: ...
    def render(self, context): ...

class GetLanguageInfoListNode(Node):
    languages = ...  # type: Any
    variable = ...  # type: Any
    def __init__(self, languages, variable) -> None: ...
    def get_language_info(self, language): ...
    def render(self, context): ...

class GetCurrentLanguageNode(Node):
    variable = ...  # type: Any
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class GetCurrentLanguageBidiNode(Node):
    variable = ...  # type: Any
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class TranslateNode(Node):
    noop = ...  # type: Any
    asvar = ...  # type: Any
    message_context = ...  # type: Any
    filter_expression = ...  # type: Any
    def __init__(self, filter_expression, noop, asvar: Optional[Any] = ..., message_context: Optional[Any] = ...) -> None: ...
    def render(self, context): ...

class BlockTranslateNode(Node):
    extra_context = ...  # type: Any
    singular = ...  # type: Any
    plural = ...  # type: Any
    countervar = ...  # type: Any
    counter = ...  # type: Any
    message_context = ...  # type: Any
    trimmed = ...  # type: Any
    asvar = ...  # type: Any
    def __init__(self, extra_context, singular, plural: Optional[Any] = ..., countervar: Optional[Any] = ..., counter: Optional[Any] = ..., message_context: Optional[Any] = ..., trimmed: bool = ..., asvar: Optional[Any] = ...) -> None: ...
    def render_token_list(self, tokens): ...
    def render(self, context, nested: bool = ...): ...

class LanguageNode(Node):
    nodelist = ...  # type: Any
    language = ...  # type: Any
    def __init__(self, nodelist, language) -> None: ...
    def render(self, context): ...

def do_get_available_languages(parser, token): ...
def do_get_language_info(parser, token): ...
def do_get_language_info_list(parser, token): ...
def language_name(lang_code): ...
def language_name_translated(lang_code): ...
def language_name_local(lang_code): ...
def language_bidi(lang_code): ...
def do_get_current_language(parser, token): ...
def do_get_current_language_bidi(parser, token): ...
def do_translate(parser, token): ...
def do_block_translate(parser, token): ...
def language(parser, token): ...
