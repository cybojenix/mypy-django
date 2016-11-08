# Stubs for django.contrib.sessions.base_session (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import models
from django.utils.translation import ugettext_lazy as _

class BaseSessionManager(models.Manager):
    def encode(self, session_dict): ...
    def save(self, session_key, session_dict, expire_date): ...

class AbstractBaseSession(models.Model):
    session_key = ...  # type: Any
    session_data = ...  # type: Any
    expire_date = ...  # type: Any
    objects = ...  # type: Any
    class Meta:
        abstract = ...  # type: bool
        verbose_name = ...  # type: Any
        verbose_name_plural = ...  # type: Any
    @classmethod
    def get_session_store_class(cls): ...
    def get_decoded(self): ...