"""
WSGI config for homelessAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from gevent import monkey; monkey.patch_all()
from psycogreen.gevent import patch_psycopg
patch_psycopg()

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homelessAPI.settings")

application = get_wsgi_application()
