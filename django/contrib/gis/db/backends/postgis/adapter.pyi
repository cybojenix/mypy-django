# Stubs for django.contrib.gis.db.backends.postgis.adapter (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PostGISAdapter:
    ewkb = ...  # type: Any
    srid = ...  # type: Any
    geography = ...  # type: Any
    def __init__(self, geom, geography: bool = ...) -> None: ...
    def __conform__(self, proto): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def prepare(self, conn): ...
    def getquoted(self): ...
