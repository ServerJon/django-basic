"""
ASGI config for django_basic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from common.code import get_env_variable

DJANGO_EXECUTION_ENVIRONMENT = get_env_variable('DJANGO_EXECUTION_ENVIRONMENT')
if DJANGO_EXECUTION_ENVIRONMENT == 'DEV':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.local")
if DJANGO_EXECUTION_ENVIRONMENT == 'PROD':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.production")

application = get_asgi_application()
