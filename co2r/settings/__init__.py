from common import *

try:
    from environment import ENVIRONMENT
except ImportError:
    ENVIRONMENT = 'DEVELOP'

try:
    if ENVIRONMENT == 'DEVELOP':
        from development import *
    elif ENVIRONMENT == 'STAGING':
        from staging import *
    elif ENVIRONMENT == 'PRODUCTION':
        from production import *
except ImportError:
    pass
