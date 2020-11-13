import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'c479uoqpw&m)us5%6q$m#%jwux3em$$jiu6xpk_+%k)u03g*ku'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
# Данные почты
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'support@skillstudy.net'
EMAIL_HOST_PASSWORD = 'Vfrc1204'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
