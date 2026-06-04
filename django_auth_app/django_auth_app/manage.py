import os
import sys


def run():
    # Point Django to the correct settings file
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth_app.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Shown when Django is not installed or venv is not active
        raise ImportError(
            "Django could not be found. "
            "Make sure it is installed and your virtual environment is active."
        )

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    run()