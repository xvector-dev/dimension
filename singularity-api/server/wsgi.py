"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
except:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings_dev")

application = get_wsgi_application()
