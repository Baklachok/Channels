"""
ASGI config for Channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from home.consumers import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Channels.settings")


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/test/', TestConsumer.as_asgi()),
            path('ws/new/', NewConsumer.as_asgi())
        ])
    )
})
