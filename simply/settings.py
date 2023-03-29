
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ktpk0*-yf2^qjm%y51kg7ke2w!f9rueqnxf@agr8rqq2*4psc$'




# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['3.225.228.167']
# ALLOWED_HOSTS = ['*']



#CSRF_TRUSTED_ORIGINS = [''] # - ADD YOUR CSRF_TRUSTED_ORIGIN




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'todo',

    'crispy_forms',

    'storages',

]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simply.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simply.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# ------ SQLite database configuration ----------- #


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# --------------------------------------------------------------- #




# ------ Amazon RDS postgres database configuration ----------- #

'''
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': '****', # - ADD YOUR DATABASE NAME FROM AMAZON RDS

        'USER': '*****', # - ADD YOUR USERNAME FROM AMAZON RDS 

        'PASSWORD': '*****', # - REMEMBER ADD YOUR PASSWORD FROM AMAZON RDS

        'HOST': '*********', # - REMEMBER ADD YOUR ENDPOINT AFTER YOUR AMAZON RDS DATABASE HAS BEEN COMPLETED

        'PORT': '5432',

    }

}
'''


# --------------------------------------------------------------- #




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DVTALLEXT',
        'USER': 'dbmasteruser',
        'PASSWORD': 'pispuser',
        'HOST': 'ls-2c19aef538b7914599d0412be9c31e84e34c493d.cs1uorlsa2xx.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
       
    }
}











# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

# Method 2 
# os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/images/'

MEDIA_ROOT = BASE_DIR / 'static/images'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ------ Amazon configuration ----------- #

#AWS_ACCESS_KEY_ID = "" # - ADD YOUR ACCESS KEY FROM IAM 
#AWS_SECRET_ACCESS_KEY = "" # - ADD YOUR SECRETY ACCESS KEY FROM IAM

# ------- Amazon S3 configuration -------------------------------#

#AWS_STORAGE_BUCKET_NAME = "" # - ADD YOUR BUCKET NAME HERE

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#AWS_S3_FILE_OVERWRITE = False # - PREVENT FILE OVERWRITES 

# ----------------------------------------- #



AWS_ACCESS_KEY_ID = "AKIAYFZLZWB5NWPM2FZK" 
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "dvt-ubuntu-bkt"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False 









