from .base import *

import environ

ALLOWED_HOSTS = ["43.200.38.56", "lg-voc.com"]
<<<<<<< HEAD
STATIC_ROOT = BASE_DIR / "static/"
=======

>>>>>>> 838073b25bf5bb942b5edb873e8d12946fae03d4
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
DEBUG = True

env = environ.Env()
<<<<<<< HEAD
environ.Env.read_env(BASE_DIR / ".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
=======
environ.Env.read_env(str(BASE_DIR / ".env"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
>>>>>>> 838073b25bf5bb942b5edb873e8d12946fae03d4
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
<<<<<<< HEAD
        "PORT": "5432",
=======
        "PORT": "3306",
>>>>>>> 838073b25bf5bb942b5edb873e8d12946fae03d4
    }
}
