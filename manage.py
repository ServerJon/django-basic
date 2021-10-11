#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from common.code import get_env_variable

def main():
    """Run administrative tasks."""
    DJANGO_EXECUTION_ENVIRONMENT = get_env_variable('DJANGO_EXECUTION_ENVIRONMENT')
    if DJANGO_EXECUTION_ENVIRONMENT == 'DEV':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.local")
    if DJANGO_EXECUTION_ENVIRONMENT == 'PROD':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_basic.settings.production")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
