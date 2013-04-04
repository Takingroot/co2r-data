DEBUG = False
TEMPLATE_DEBUG = False

STATIC_URL = 'http://data.co2r.com/static/'

try:
    from production_local import *
except ImportError:
    pass
