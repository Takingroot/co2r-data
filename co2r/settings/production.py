DEBUG = False
TEMPLATE_DEBUG = False
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://ubuntu:abc123@localhost/co2r')}
