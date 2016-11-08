# Stubs for django.views.decorators.csrf (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.middleware.csrf import CsrfViewMiddleware

csrf_protect = ...  # type: Any

class _EnsureCsrfToken(CsrfViewMiddleware): ...

requires_csrf_token = ...  # type: Any

class _EnsureCsrfCookie(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs): ...

ensure_csrf_cookie = ...  # type: Any

def csrf_exempt(view_func): ...