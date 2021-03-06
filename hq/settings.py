import django_heroku,dj_database_url
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kt_*yi1px_k5%z^)#5kn&0ste+are41_rl_eia6o&y+nu9d*=w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost" , "0.0.0.0" , "hiqwebapp.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'login',
    'events',
    'uprofile',
    'home',
    'signup',
    'upload_pro',
    'logout',
    'gallery',
    'Feeds',
    'comments',
    'suggestions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'hq.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR , "login/templates/login"),
                os.path.join(BASE_DIR , "signup/templates/signup"),
                os.path.join(BASE_DIR , "events/templates/events"),
                os.path.join(BASE_DIR , "uprofile/templates/uprofile"),
                os.path.join(BASE_DIR , "upload_pro/templates/upload_pro"),
                os.path.join(BASE_DIR , "logout/templates/logout"),
                os.path.join(BASE_DIR , "gallery/templates/gallery"),
                os.path.join(BASE_DIR , "Feeds/templates/Feeds"),
                os.path.join(BASE_DIR , "hq/templates/"),
                os.path.join(BASE_DIR , "comments/templates/"),
                os.path.join(BASE_DIR , "suggestions/templates/"),
                ],
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

WSGI_APPLICATION = 'hq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'hq_testdbs',
#         'HOST':'127.0.0.1',
#         'USER':'root',
#         'PASSWORD':''
#     }
# }
#

cloudinary.config(
    cloud_name = "hnrzh8e6y",
    api_key = "155398246326869",
    api_secret = "DvstqWdcXyvYw1V-F94yAPReib4"
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'hq.sqlite3'),
    }
}


db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)

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

# TIME_ZONE = "UTC"
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR , "static_root/")

STATICFILES_DIRS = [
os.path.join(BASE_DIR , "signup/static/"),
os.path.join(BASE_DIR , "events/static/"),
os.path.join(BASE_DIR , "uprofile/static/"),
os.path.join(BASE_DIR , "upload_pro/static/"),
os.path.join(BASE_DIR , "logout/static/"),
os.path.join(BASE_DIR , "login/static/"),
os.path.join(BASE_DIR , "gallery/static/"),
os.path.join(BASE_DIR , "Feeds/static/"),
os.path.join(BASE_DIR , "hq/static/"),
os.path.join(BASE_DIR , "comments/static/"),
os.path.join(BASE_DIR , "suggestions/static/"),
]




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , "media_root/")
# MEDIA_ROOT = os.path.join(BASE_DIR , "media_root/")
django_heroku.settings(locals())
