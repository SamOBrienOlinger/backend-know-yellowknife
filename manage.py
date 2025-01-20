#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Add the project root directory (where manage.py is located) to sys.path
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_path)

    # Add the parent directory (for the 'backend' module) to sys.path
    project_root = os.path.dirname(current_path)
    sys.path.append(project_root)

    # Set the default Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
