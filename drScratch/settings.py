#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

from django.conf import global_settings

"""
Django settings for drScratch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = '/static/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&0vhl+ghtc+31i7xmq@$t)n^)*8p3a9!p8=pk2z9tb5om*(&l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',

#'django.template.loaders.eggs.Loader',
)


TEMPLATE_DIRS = ('templates',)

ALLOWED_HOSTS = ['localhost', '193.147.51.252','drscratchpre.programamos.es']




# Application definition

INSTALLED_APPS = (
    'app',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'drScratch.urls'

WSGI_APPLICATION = 'drScratch.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drscratch',
	'USER': 'root',
	'PASSWORD': 'Mysql.drscratch',
	'HOST': 'localhost',
	'PORT': '',
	'OPTIONS':{
		'autocommit': True,
	}
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'static'

# Internationalization

# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

_ = lambda s: s

LANGUAGES = (
    ('es', _('Español')),
    ('en', _('English')),
    ('ca', _('Catalán')),
    ('gl', _('Gallego')),
    ('eu', _('Vasco')),
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

