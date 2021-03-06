# Stubs for django.contrib.auth.views (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.utils.translation import ugettext as _

def deprecate_current_app(func): ...
def login(request, template_name: str = ..., redirect_field_name: Any = ..., authentication_form: Any = ..., extra_context: Optional[Any] = ...): ...
def logout(request, next_page: Optional[Any] = ..., template_name: str = ..., redirect_field_name: Any = ..., extra_context: Optional[Any] = ...): ...
def logout_then_login(request, login_url: Optional[Any] = ..., extra_context: Optional[Any] = ...): ...
def redirect_to_login(next, login_url: Optional[Any] = ..., redirect_field_name: Any = ...): ...
def password_reset(request, is_admin_site: bool = ..., template_name: str = ..., email_template_name: str = ..., subject_template_name: str = ..., password_reset_form: Any = ..., token_generator: Any = ..., post_reset_redirect: Optional[Any] = ..., from_email: Optional[Any] = ..., extra_context: Optional[Any] = ..., html_email_template_name: Optional[Any] = ..., extra_email_context: Optional[Any] = ...): ...
def password_reset_done(request, template_name: str = ..., extra_context: Optional[Any] = ...): ...
def password_reset_confirm(request, uidb64: Optional[Any] = ..., token: Optional[Any] = ..., template_name: str = ..., token_generator: Any = ..., set_password_form: Any = ..., post_reset_redirect: Optional[Any] = ..., extra_context: Optional[Any] = ...): ...
def password_reset_complete(request, template_name: str = ..., extra_context: Optional[Any] = ...): ...
def password_change(request, template_name: str = ..., post_change_redirect: Optional[Any] = ..., password_change_form: Any = ..., extra_context: Optional[Any] = ...): ...
def password_change_done(request, template_name: str = ..., extra_context: Optional[Any] = ...): ...
