# Stubs for django.contrib.flatpages.models (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import models
from django.utils.translation import ugettext_lazy as _

class FlatPage(models.Model):
    url = ...  # type: Any
    title = ...  # type: Any
    content = ...  # type: Any
    enable_comments = ...  # type: Any
    template_name = ...  # type: Any
    registration_required = ...  # type: Any
    sites = ...  # type: Any
    class Meta:
        db_table = ...  # type: str
        verbose_name = ...  # type: Any
        verbose_name_plural = ...  # type: Any
        ordering = ...  # type: Any
    def get_absolute_url(self): ...