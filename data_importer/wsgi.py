"""
WSGI config for data_importer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_importer.settings")

application = get_wsgi_application()
