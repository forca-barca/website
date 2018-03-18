import os
import sys
from django.core.wsgi import get_wsgi_application
path = '/home/AiHiringv1/website'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']='website.settings'

from django.contrib.staticfiles.handlers import StaticFilesHandler
appliaction=StaticFilesHandler(get_wsgi_application())