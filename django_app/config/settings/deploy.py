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

print('===== DEBUG', DEBUG)
print('===== ALLOWED_HOSTS', ALLOWED_HOSTS)