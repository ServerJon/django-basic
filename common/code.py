import os
import json

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
        raise ImproperlyConfigured(error_msg) from KeyError


def get_secret(secret_name):
    """Get the main values from the secret.json file

    Args:
        secret_name (str): The secret value to receive

    Raises:
        ImproperlyConfigured: Error if we don't find the value

    Returns:
        str: The selected value
    """

    # Get the secret dict
    with open("secret.json") as _file:
        secret_data = json.loads(_file.read())

    try:
        return secret_data[secret_name]
    except BaseException:
        msg = "la variable {} no existe".format(secret_name)
        raise ImproperlyConfigured(msg) from None
