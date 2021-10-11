import os

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """Get a global environment variable

    Args:
        var_name (str): Variable name

    Raises:
        ImproperlyConfigured: Error if not find the variable

    Returns:
        str: Variable value
    """

    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)