"""
Django settings for proto_app project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import logging.config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# to generate secret key run
# LC_ALL=C </dev/urandom tr -dc 'A-Za-z0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' | head -c 50 && echo
DEBUG = os.getenv('DJANGO_DEBUG', True)

if DEBUG == True:
    SECRET_FILE = os.path.join(BASE_DIR, 'secret_key.txt')
    with open(SECRET_FILE) as f:
        SECRET_KEY = f.read().strip()
else:
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # this app is apparently required by Django AllAuth. No more details...


    # application apps
    'application',
    'settings',
    'accounts',

    # third party tools
    'ckeditor',
    'crispy_forms',

    # this app must be last to have proper file cleanup
    'django_cleanup.apps.CleanupConfig',


    # allauth applications
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # allauth providers
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google'


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

ROOT_URLCONF = 'proto_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # templates at root level. We may want to place separate templates in each app...,
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

# The AUTH USER MODEL TELLS DJANGO WHAT TO AUTHENTICATE ON - OTHERWISE THERE WILL BE ERRORS
AUTH_USER_MODEL = 'accounts.User_Account'

WSGI_APPLICATION = 'proto_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG == True:
    DB_PATH = BASE_DIR
else:
    DB_PATH = os.getenv('DJANGO_DATABASE_PATH')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_PATH, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

if DEBUG == True:
    STATIC_FILE_PATH = BASE_DIR
    MEDIA_FILE_PATH = BASE_DIR
else:
    STATIC_FILE_PATH = os.getenv('DJANGO_STATIC_PATH')
    MEDIA_FILE_PATH = os.getenv('DJANGO_MEDIA_PATH')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(STATIC_FILE_PATH, 'static_assets/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_data/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(MEDIA_FILE_PATH, 'media_assets/')


# CKEDITOR RICH TEXT EDITOR SETTING
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                    ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                    'JustifyRight', 'JustifyBlock'],
                    ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
                    ],
        'width': 'auto',
    },
}


# The parameters below are from the AllAuth Social Login.
# this is the first site ID (default) required by the Django Contrib Sites app
SITE_ID = 1

LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
SOCIALACCOUNT_ADAPTER = 'accounts.adapters.ProperSocialAccountAdapter'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"


# Logging Configuration
# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(message)s',
        },
        'django': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'django',
            'filename': 'proto_app.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': LOGLEVEL,
            'propagate': True,
        },
    },
})
