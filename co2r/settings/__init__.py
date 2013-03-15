from common import *

try:
    from environment import ENVIRONMENT
except ImportError:
    ENVIRONMENT = 'DEVELOP'

try:
    if environment == 'DEVELOP':
        from development import *
    elif environment == 'STAGING':
        from staging import *
    elif environment == 'PRODUCTION':
        from production import *
except ImportError:
    pass
