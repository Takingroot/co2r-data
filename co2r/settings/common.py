import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.path.pardir,\
     os.path.pardir, os.path.pardir))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pierre Drescher', 'pierre.drescher+takingroot@gmail.com'),
)

TAKINGROOT_STAFF = (
    ('Pierre', 'pierre.drescher@gmail.com'),
    ('Brooke', 'brooke@takingroot.org'),
)

if DEBUG == True:
    TAKINGROOT_STAFF = (
        ('Pierre', 'pierre.drescher@gmail.com'),
        ('Jason', 'jasonkuhrt@me.com')
    )   

EMAIL_SENDER = 'Taking Root <info@takingroot.org>'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@takingroot.mailgun.org'
EMAIL_HOST_PASSWORD = '2-zrh1w3xhm7'
EMAIL_PORT = 587

MANAGERS = ADMINS

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost/co2r')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Canada/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('fr-ca', 'French'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://data.co2r.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(PROJECT_ROOT, 'public'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '6cs3^_oje@nq79g!bfpm*brq5$$swzs4dh=vypha#z!j=_$erc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dynamicresponse.middleware.api.APIMiddleware',
    'co2r.middleware.Co2rMiddleware',
)

ROOT_URLCONF = 'co2r.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'co2r.wsgi.application'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

INSTALLED_APPS = (
    'responsive_admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'co2r.main',
    'co2r.artifacts',
    'co2r.organizations',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

RESPONSIVE_ADMIN_FIXED_SUBMIT_LINE = True

ALLOWED_HOSTS = ['data.co2r.com', '*.herokuapp.com']