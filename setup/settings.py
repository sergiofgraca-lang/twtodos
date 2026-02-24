import os
from pathlib import Path
from decouple import Config, RepositoryEnv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔥 FORÇA O CAMINHO DO .env
env = Config(RepositoryEnv(BASE_DIR / ".env"))

# ==============================
# SEGURANÇA
# ==============================

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = env(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost'
).split(',')

# ==============================
# APLICAÇÕES
# ==============================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'todos',  # seu app
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

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'setup.wsgi.application'

# ==============================
# BANCO DE DADOS (POSTGRESQL)
# ==============================

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL")
    )
}
# ==============================
# VALIDAÇÃO DE SENHA
# ==============================

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

# ==============================
# INTERNACIONALIZAÇÃO
# ==============================

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

# ==============================
# ARQUIVOS ESTÁTICOS
# ==============================

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'