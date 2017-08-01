# deploy.py
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# DEBUG MODE
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = config_secret_deploy['django']['databases']

print('===== DEBUG', DEBUG)
print('===== ALLOWED_HOSTS', ALLOWED_HOSTS)