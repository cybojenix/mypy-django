# Stubs for django.core.serializers.pyyaml (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.serializers.python import Deserializer as PythonDeserializer, Serializer as PythonSerializer
from yaml import CSafeLoader as SafeLoader
from yaml import CSafeDumper as SafeDumper
from yaml import SafeDumper

class DjangoSafeDumper(SafeDumper):
    def represent_decimal(self, data): ...
    def represent_ordered_dict(self, data): ...

class Serializer(PythonSerializer):
    internal_use_only = ...  # type: bool
    def handle_field(self, obj, field): ...
    def end_serialization(self): ...
    def getvalue(self): ...

def Deserializer(stream_or_string, **options): ...
