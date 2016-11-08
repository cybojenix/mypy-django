# Stubs for django.contrib.admin.forms (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _

class AdminAuthenticationForm(AuthenticationForm):
    error_messages = ...  # type: Any
    required_css_class = ...  # type: str
    def confirm_login_allowed(self, user): ...

class AdminPasswordChangeForm(PasswordChangeForm):
    required_css_class = ...  # type: str
