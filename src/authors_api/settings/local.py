from .base import * #noqa
from .base import env #noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="WgUxDDtRN81H2i8IM7hdZoJuzwjZKrqkICpjPJEqm41vf8e2AIo",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

ALLOWED_HOSTS = []