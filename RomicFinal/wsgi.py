
import os
import sys

from django.core.wsgi import get_wsgi_application

project_home = '/home/a/RomicCare/'

if project_home not in  sys.path:
	sys.path.insert(0 , project_home)
	pass


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RomicFinal.settings')

application = get_wsgi_application()
