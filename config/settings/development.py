"""
Django settings for {{ project_name }} project in development mode

This fill will be automatically used when using `manage.py`.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""


from .base import *


DEBUG = True

# for development, we don't need password validation
AUTH_PASSWORD_VALIDATORS = []
