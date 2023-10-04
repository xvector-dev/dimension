"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

try:
    django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
except:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings_dev")

application = get_asgi_application()
