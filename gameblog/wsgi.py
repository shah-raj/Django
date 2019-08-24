"""
WSGI config for gameblog project.

It exposes the WSGI callable as a module-level variable named ``game``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gameblog.settings")

application = get_wsgi_application()
