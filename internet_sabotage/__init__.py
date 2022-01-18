# -*- coding: utf-8 -*-

import socket
import sys

from contextdecorator import ContextDecorator


class no_connection(ContextDecorator):
    _module = sys.modules[__name__]

    def __init__(self, exception=IOError):
        self.exception = exception

    def _enable_socket(self):
        setattr(self._module, '_socket_disabled', False)

    def _disable_socket(self):
        setattr(self._module, '_socket_disabled', True)

        def guarded(*args, **kwargs):
            if getattr(self._module, '_socket_disabled', False):
                raise self.exception('Internet is disabled')

            return socket.SocketType(*args, **kwargs)

        socket.socket = guarded

    def __enter__(self):
        self._disable_socket()

    def __exit__(self, *exc_details):
        self._enable_socket()
