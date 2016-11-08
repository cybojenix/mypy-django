# Stubs for django.contrib.sites.models (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import models
from django.utils.translation import ugettext_lazy as _

SITE_CACHE = ...  # type: Any

class SiteManager(models.Manager):
    use_in_migrations = ...  # type: bool
    def get_current(self, request: Optional[Any] = ...): ...
    def clear_cache(self): ...

class Site(models.Model):
    domain = ...  # type: Any
    name = ...  # type: Any
    objects = ...  # type: Any
    class Meta:
        db_table = ...  # type: str
        verbose_name = ...  # type: Any
        verbose_name_plural = ...  # type: Any
        ordering = ...  # type: Any

def clear_site_cache(sender, **kwargs): ...
