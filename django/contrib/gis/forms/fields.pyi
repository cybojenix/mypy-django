# Stubs for django.contrib.gis.forms.fields (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import forms
from django.utils.translation import ugettext_lazy as _
from .widgets import OpenLayersWidget as OpenLayersWidget

class GeometryField(forms.Field):
    widget = ...  # type: Any
    geom_type = ...  # type: str
    default_error_messages = ...  # type: Any
    srid = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...
    def to_python(self, value): ...
    def clean(self, value): ...
    def has_changed(self, initial, data): ...

class GeometryCollectionField(GeometryField):
    geom_type = ...  # type: str

class PointField(GeometryField):
    geom_type = ...  # type: str

class MultiPointField(GeometryField):
    geom_type = ...  # type: str

class LineStringField(GeometryField):
    geom_type = ...  # type: str

class MultiLineStringField(GeometryField):
    geom_type = ...  # type: str

class PolygonField(GeometryField):
    geom_type = ...  # type: str

class MultiPolygonField(GeometryField):
    geom_type = ...  # type: str
