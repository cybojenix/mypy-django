# Stubs for django.templatetags.cache (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.template import Node

register = ...  # type: Any

class CacheNode(Node):
    nodelist = ...  # type: Any
    expire_time_var = ...  # type: Any
    fragment_name = ...  # type: Any
    vary_on = ...  # type: Any
    cache_name = ...  # type: Any
    def __init__(self, nodelist, expire_time_var, fragment_name, vary_on, cache_name) -> None: ...
    def render(self, context): ...

def do_cache(parser, token): ...
