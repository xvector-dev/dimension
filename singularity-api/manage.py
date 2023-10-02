#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json


def main():
    """Run administrative tasks."""
    # secret_json = os.environ.get('DJANGO_SETTINGS_MODULE')
    # # Parse the JSON to get individual values
    # secret_data = json.loads(secret_json)
    # django_settings_module = secret_data.get('DJANGO_SETTINGS_MODULE')

    # if not django_settings_module:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings_dev")
    # else:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings_prod")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
