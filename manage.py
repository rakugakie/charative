#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":

    ROOT_DIR = os.environ.Path(__file__) - 3
    env = os.environ.Env(DEBUG=(bool, False), )

    READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

    if READ_DOT_ENV_FILE:
        # Operating System Environment variables have precedence over variables defined in the .env file,
        # that is to say variables from the .env files will only be used if not defined
        # as environment variables.
        env_file = str(ROOT_DIR.path('.env'))
        print('Loading : {}'.format(env_file))
        env.read_env(env_file)
        print('The .env file has been loaded from manage.py. See base.py for more information')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
