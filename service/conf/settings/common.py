"""
common project settings
"""

import environ
import pymongo


env = environ.Env()

BASE_DIR = environ.Path(__file__) - 3

DEBUG = env.bool('DJANGO_DEBUG', default=False)

MONGO_URI = env('MONGO_URI', default="mongodb://localhost:27017/")
DBNAME = env('MONGO_DATABASE_NAME', default="twitter")

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

SECRET_KEY = env('DJANGO_SECRET_KEY', default='_y=vx5zc8$1@t%#8qq&6nq#q$hdkoixcqlq!f*-2$98@zrvkoh')

# connect to mongodb 
MONGO = pymongo.MongoClient(MONGO_URI)
DB = MONGO[DBNAME]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    'rest_framework',
]

PROJECT_APPS = [
    "twitter",
]

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TWITTER_CONSUMER_KEY = env('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = env('TWITTER_CONSUMER_SECRET')
MAX_TWEETS_COUNT = env.int('MAX_TWEETS_COUNT', default=200)

CELERY_BROKER_URL = env('CELERY_REDIS_BROKER', default='redis://localhost:6379/0')

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
