DEBUG = False
TEMPLATE_DEBUG = False

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://ubuntu:abc123@localhost/co2r')}

STATIC_URL = 'http://data.co2r.com/static/'

try:
    from production_local import *
except ImportError:
    pass
