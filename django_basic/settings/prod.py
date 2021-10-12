from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]", "0.0.0.0"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": get_secret('DB_NAME'),
        "USER": get_secret('USER_DB'),
        "PASSWORD": get_secret('PWD_DB'),
        "HOST": get_env_variable("DATABASE_HOST"),
        "PORT": "3306",
    }
}

# Static Django admin web files

STATIC_ROOT = BASE_DIR.child('staticfiles')
