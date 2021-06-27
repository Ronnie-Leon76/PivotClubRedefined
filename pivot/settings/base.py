<<<<<<< HEAD
"""
Django settings for pivot project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from pathlib import Path

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_DIR = BASE_DIR / 'static'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
TEMPLATE_DIR = BASE_DIR / 'templates'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # new modules apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary',
    'crispy_forms',
    'widget_tweaks',

    # project apps
    'accounts.apps.AccountsConfig',
    'main',
    'blog',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pivot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'pivot.wsgi.application'

# Authentication Backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
=======
"""Django settings for pivot project.Generated by 'django-admin startproject' using Django 2.2.6.For more information on this file, seehttps://docs.djangoproject.com/en/2.2/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/2.2/ref/settings/"""from pathlib import Pathimport cloudinaryimport osfrom decouple import config# Build paths inside the project like this: os.path.join(BASE_DIR, ...)BASE_DIR = Path(__file__).resolve().parent.parent.parentSTATIC_DIR = BASE_DIR / 'static'STATIC_ROOT = BASE_DIR / 'staticfiles'MEDIA_ROOT = BASE_DIR / 'media'TEMPLATE_DIR = BASE_DIR / 'templates'# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = config('SECRET_KEY')ALLOWED_HOSTS = ['*']# Application definitionINSTALLED_APPS = [    # django apps    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.sites',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    # new modules apps    'allauth',    'allauth.account',    'allauth.socialaccount',    'allauth.socialaccount.providers.google',    'cloudinary',    'rangefilter',    'widget_tweaks',    # project apps    'accounts.apps.AccountsConfig',    'main',    'blog',]SITE_ID = 1SOCIALACCOUNT_PROVIDERS = {    'google': {        'SCOPE': [            'profile',            'email',        ],        'AUTH_PARAMS': {            'access_type': 'online',        }    }}MIDDLEWARE = [    'django.middleware.security.SecurityMiddleware',    'whitenoise.middleware.WhiteNoiseMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',]ROOT_URLCONF = 'pivot.urls'TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [            TEMPLATE_DIR        ],        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',                'django.template.context_processors.request',            ],        },    },]WSGI_APPLICATION = 'pivot.wsgi.application'# Authentication BackendsAUTHENTICATION_BACKENDS = (    'django.contrib.auth.backends.ModelBackend',    'allauth.account.auth_backends.AuthenticationBackend',)# Password validation# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]# Internationalization# https://docs.djangoproject.com/en/2.2/topics/i18n/LANGUAGE_CODE = 'en-us'TIME_ZONE = 'UTC'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = TrueDEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/2.2/howto/static-files/STATIC_URL = '/static/'# Extra places for collectstatic to find static files.STATICFILES_DIRS = (    os.path.join(BASE_DIR, 'static'),)MEDIA_URL = '/media/'AUTHENTICATION_BACKENDS = (    'django.contrib.auth.backends.ModelBackend',    'allauth.account.auth_backends.AuthenticationBackend',)cloudinary.config(    cloud_name=config('CLOUD_NAME'),    api_key=config('CLOUDINARY_API_KEY'),    api_secret=config('CLOUDINARY_API_SECRET'))ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1ACCOUNT_EMAIL_REQUIRED = TrueACCOUNT_EMAIL_VERIFICATION = "mandatory"ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'LOGIN_REDIRECT_URL = '/accounts/email/'
>>>>>>> 313c9d92cd112350f101e71a3d2e08d11835faf7
