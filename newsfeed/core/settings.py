from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure--5l$i_zkpefix-w$#@!+pkpg96h71*t=se^k$(41pu!5m=j6)w'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'widget_tweaks',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'news',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context_processor.latest_news',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
    'minimal': {  # minimal toolbar konfiguratsiyasi
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],       # matnni qalin, kursiv, ostiga chizish
            ['NumberedList', 'BulletedList'],      # ro‘yxatlar
            ['Link', 'Unlink'],                    # link qo‘shish
            ['RemoveFormat'],                       # formatni olib tashlash
        ],
        'height': 200,
        'width': '100%',
        'removePlugins': 'stylesheetparser',
    },
     '15_buttons_config': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', '-', 'Save', 'NewPage', 'Preview'],       # 5 ta tugma
            ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo'],       # 4 ta tugma (+ ayirgichlar)
            ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat'], # 5 ta tugma
            ['Link', 'Unlink'],                                  # 2 ta tugma (jami 16 ta bo'ldi, Unlinkni olib tashladim 15 qilish uchun)
        ],
        'width': '100%',
        'height': 200,
        'removePlugins': 'stylesheetparser',
        'extraPlugins': ','.join([
            'uploadimage', # Rasm yuklash plaginini qo'shish
            'div',
            'autolink',
            'autoembed',
            'rename_caption',
        ]),
    }
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True


# settings.py
LOGIN_REDIRECT_URL = '/'  # login bo‘lgach user shu URL ga yuboriladi
LOGIN_REDIRECT_URL = '/'  # agar dashboard app bo‘lsa


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'


LOGIN_REDIRECT_URL = '/accounts/profile-redirect/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

LOGIN_URL = '/accounts/login/'