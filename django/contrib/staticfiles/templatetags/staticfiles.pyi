# Stubs for django.contrib.staticfiles.templatetags.staticfiles (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.templatetags.static import StaticNode

register = ...  # type: Any

def static(path): ...

class StaticFilesNode(StaticNode):
    def url(self, context): ...

def do_static(parser, token): ...
