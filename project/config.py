# project/config.py
"""Project configuration."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.abspath(os.path.join(os.path.dirname(basedir), 'data'))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = "Application name"
    SECRET_KEY = "Change this SECRET_KEY, because it's not secret anymore."
    ADMINS = frozenset(['admin@example.com'])  # change this...

    DEBUG = False
    DEBUG_TB_ENABLED = False
    PROPAGATE_EXCEPTIONS = False

    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "A random secret key should be put here."

    BOOTSTRAP_QUERYSTRING_REVVING = True
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    DATABASE_CONNECT_OPTIONS = {}

    SEND_FILE_MAX_AGE_DEFAULT = 2592000  # seconds file is cached by browser
    USE_X_SENDFILE = True

    THREADS_PER_PAGE = 8

    BABEL_DEFAULT_LOCALE = "en_GB"
    BABEL_DEFAULT_TIMEZONE = "UTC"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + datadir + "/dev.sqlite"
    SQLALCHEMY_ECHO = True

    SEND_FILE_MAX_AGE_DEFAULT = 1  # 1 second file is cached by browser
    USE_X_SENDFILE = False


class TestingConfig(DevelopmentConfig):
    """Testing configuration."""

    TESTING = True
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = "postgresql:///user@localhost:5432/example"
    DATABASE_CONNECT_OPTIONS = {}
