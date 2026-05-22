# =========================
# PYMySQL / MariaDB COMPATIBILITY FIX (MUST BE FIRST) installed_March9
# =========================
# import pymysql

# pymysql.version_info = (2, 2, 1, "final", 0)
# pymysql.install_as_MySQLdb()

"""Django settings for the ecommerce project.

This project implements a multi-vendor ecommerce system
with buyer product browsing, session-based carts,
checkout with email invoices, and verified product reviews."""

# =========================
# STANDARD DJANGO SETTINGS
# =========================
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY / DEBUG
# =========================
SECRET_KEY = "django-insecure-plpa_=6_yj3a=b74lo4s&ly6qe=j2gtbg=3jb7!8q^(8$b*e8#"

DEBUG = True

ALLOWED_HOSTS = []


# =========================
# APPLICATION DEFINITION
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Project apps
    "products.apps.ProductsConfig",
    "stores.apps.StoresConfig",
    "widget_tweaks",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# URL / TEMPLATE CONFIG
# =========================
ROOT_URLCONF = "ecommerce_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce_project.wsgi.application"


# =========================
# DATABASE (MariaDB – WORKING)
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce_db",
        "USER": "root",
        "PASSWORD": "Disney2Disney",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# =========================
# AUTH / LOGIN (USER-FACING)
# =========================
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/products/"
LOGOUT_REDIRECT_URL = "/"


# =========================
# STATIC FILES
# =========================
STATIC_URL = "static/"
# Add extra directories here for global static assets (optional)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# =========================
# DEFAULT PRIMARY KEY
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================
# EMAIL (DEV ONLY)
# =========================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@ecommerce.local"
