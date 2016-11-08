# Stubs for django.core.urlresolvers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.http import Http404

class ResolverMatch:
    func = ...  # type: Any
    args = ...  # type: Any
    kwargs = ...  # type: Any
    url_name = ...  # type: Any
    app_names = ...  # type: Any
    app_name = ...  # type: Any
    namespaces = ...  # type: Any
    namespace = ...  # type: Any
    view_name = ...  # type: Any
    def __init__(self, func, args, kwargs, url_name: Optional[Any] = ..., app_names: Optional[Any] = ..., namespaces: Optional[Any] = ...) -> None: ...
    def __getitem__(self, index): ...

class Resolver404(Http404): ...
class NoReverseMatch(Exception): ...

def get_callable(lookup_view, can_fail: bool = ...): ...
def get_resolver(urlconf: Optional[Any] = ...): ...
def get_ns_resolver(ns_pattern, resolver): ...
def get_mod_func(callback): ...

class LocaleRegexProvider:
    def __init__(self, regex) -> None: ...
    @property
    def regex(self): ...

class RegexURLPattern(LocaleRegexProvider):
    default_args = ...  # type: Any
    name = ...  # type: Any
    def __init__(self, regex, callback, default_args: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def add_prefix(self, prefix): ...
    def resolve(self, path): ...
    @property
    def callback(self): ...

class RegexURLResolver(LocaleRegexProvider):
    urlconf_name = ...  # type: Any
    callback = ...  # type: Any
    default_kwargs = ...  # type: Any
    namespace = ...  # type: Any
    app_name = ...  # type: Any
    def __init__(self, regex, urlconf_name, default_kwargs: Optional[Any] = ..., app_name: Optional[Any] = ..., namespace: Optional[Any] = ...) -> None: ...
    @property
    def reverse_dict(self): ...
    @property
    def namespace_dict(self): ...
    @property
    def app_dict(self): ...
    def resolve(self, path): ...
    def urlconf_module(self): ...
    def url_patterns(self): ...
    def resolve_error_handler(self, view_type): ...
    def reverse(self, lookup_view, *args, **kwargs): ...

class LocaleRegexURLResolver(RegexURLResolver):
    def __init__(self, urlconf_name, default_kwargs: Optional[Any] = ..., app_name: Optional[Any] = ..., namespace: Optional[Any] = ...) -> None: ...
    @property
    def regex(self): ...

def resolve(path, urlconf: Optional[Any] = ...): ...
def reverse(viewname, urlconf: Optional[Any] = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ..., current_app: Optional[Any] = ...): ...

reverse_lazy = ...  # type: Any

def clear_url_caches(): ...
def set_script_prefix(prefix): ...
def get_script_prefix(): ...
def clear_script_prefix(): ...
def set_urlconf(urlconf_name): ...
def get_urlconf(default: Optional[Any] = ...): ...
def is_valid_path(path, urlconf: Optional[Any] = ...): ...
def translate_url(url, lang_code): ...