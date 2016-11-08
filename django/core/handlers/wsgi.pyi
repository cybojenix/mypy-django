# Stubs for django.core.handlers.wsgi (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import http
import base

logger = ...  # type: Any
ISO_8859_1 = ...  # type: Any
UTF_8 = ...  # type: Any

class LimitedStream:
    stream = ...  # type: Any
    remaining = ...  # type: Any
    buffer = ...  # type: bytes
    buf_size = ...  # type: Any
    def __init__(self, stream, limit, buf_size: Any = ...) -> None: ...
    def read(self, size: Optional[Any] = ...): ...
    def readline(self, size: Optional[Any] = ...): ...

class WSGIRequest(http.HttpRequest):
    environ = ...  # type: Any
    path_info = ...  # type: Any
    path = ...  # type: Any
    META = ...  # type: Any
    method = ...  # type: Any
    encoding = ...  # type: Any
    resolver_match = ...  # type: Any
    def __init__(self, environ) -> None: ...
    def GET(self): ...
    def COOKIES(self): ...
    POST = ...  # type: Any
    FILES = ...  # type: Any

class WSGIHandler(base.BaseHandler):
    initLock = ...  # type: Any
    request_class = ...  # type: Any
    def __call__(self, environ, start_response): ...

def get_path_info(environ): ...
def get_script_name(environ): ...
def get_bytes_from_wsgi(environ, key, default): ...
def get_str_from_wsgi(environ, key, default): ...
