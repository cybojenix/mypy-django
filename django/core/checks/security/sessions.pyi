# Stubs for django.core.checks.security.sessions (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def add_session_cookie_message(message): ...

W010 = ...  # type: Any
W011 = ...  # type: Any
W012 = ...  # type: Any

def add_httponly_message(message): ...

W013 = ...  # type: Any
W014 = ...  # type: Any
W015 = ...  # type: Any

def check_session_cookie_secure(app_configs, **kwargs): ...
def check_session_cookie_httponly(app_configs, **kwargs): ...
