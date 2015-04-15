"""
Django settings for MarkovLyrics project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ceuciwd&yfe&xnwh1hbq+bfg7%-e5ip$ft21(4*(py@g%^rii4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Generator'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MarkovLyrics.urls'

WSGI_APPLICATION = 'MarkovLyrics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": "random",
        "USER": "sam",
        "PASSWORD": '',
        "HOST": 'localhost',
        "PORT": '',
    }
}




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATABASE_URL = "postgres://sam@localhost:5432/random"

# Allow all host headers
# Parse database configuration from $DATABASE_URL
import dj_database_url
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'postgres://sam@localhost/random'

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['serene-dawn-4963.herokuapp.com']
#ALLOWED_HOSTS = ['*']
# Static asset configuration


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



