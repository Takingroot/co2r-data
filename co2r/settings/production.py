DEBUG = False
TEMPLATE_DEBUG = False

try:
    from production_local import *
except ImportError:
    pass
