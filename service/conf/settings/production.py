from conf.settings.common import *


INSTALLED_APPS += [
    'gunicorn',
    'corsheaders',
]

CORS_ORIGIN_ALLOW_ALL = env.bool('DJANGO_CORS_ORIGIN_ALLOW_ALL', default=False)
CORS_ALLOW_CREDENTIALS = env.bool('DJANGO_CORS_ALLOW_CREDENTIALS', default=False)
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST', default=[])

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
