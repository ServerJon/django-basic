"""
WSGI config for django_basic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from common.code import get_env_variable

DJANGO_EXECUTION_ENVIRONMENT = get_env_variable('DJANGO_EXECUTION_ENVIRONMENT')
if DJANGO_EXECUTION_ENVIRONMENT == 'DEV':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.local")
if DJANGO_EXECUTION_ENVIRONMENT == 'PROD':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.production")

application = get_wsgi_application()
