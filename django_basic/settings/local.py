from .base import get_secret, get_env_variable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": get_secret("DB_NAME"),
        "USER": get_secret("USER_DB"),
        "PASSWORD": get_secret("PWD_DB"),
        "HOST": get_env_variable("DATABASE_HOST"),
        "PORT": "3306",
    }
}
