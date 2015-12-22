"""
Django settings for photo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import MySQLdb
import sae
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2-8lq#wtyf)b)s$kgg(ak12f2!#&a#rgr8gu-2oxrg$@xo-o)q'

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
    'django.contrib.staticfiles',
    'img',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'photo.urls'

WSGI_APPLICATION = 'photo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': sae.const.MYSQL_DB,
	'USER': sae.const.MYSQL_USER,
	'PASSWORD': sae.const.MYSQL_PASS,
	'HOST': sae.const.MYSQL_HOST,
	'PORT': sae.const.MYSQL_PORT,
	}
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/start/'
TEMPLATE_DIRS = ('./img/',)

MEDIA_ROOT = '/data1/www/htdocs/825/lllcccfff/1/img'
STATIC_ROOT = '/data1/www/htdocs/825/lllcccfff/1/img'


STATICFILES_DIRS = (  
    # Put strings here, like "/home/html/static" or "C:/www/django/static".  
    # Always use forward slashes, even on Windows.  
    # Don't forget to use absolute paths, not relative paths.  
  
)  

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760


DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'

STORAGE_BUCKET_NAME = 'abc'
# ref: https://docs.djangoproject.com/en/dev/topics/files/





