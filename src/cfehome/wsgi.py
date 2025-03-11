"""
WSGI config for cfehome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

# Get the default WSGI application
application = get_wsgi_application()

# Wrap the application with WhiteNoise to serve static files
application = WhiteNoise(application, root="/path/to/static/files")

