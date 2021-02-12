"""
WSGI config for Analysis_of_Women_Safety project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
path = '/home/narasimha/womensafety'
from django.core.wsgi import get_wsgi_application

if path not in sys.path:
	sys.path.insert(0,path)
	
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Analysis_of_Women_Safety.settings")

application = get_wsgi_application()
