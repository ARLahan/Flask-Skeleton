# project/config.py
"""Project configuration."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.abspath(os.path.join(os.path.dirname(basedir), 'data'))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = "Application name"
    SECRET_KEY = "Change this SECRET_KEY, because it's not secret anymore."
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    BOOTSTRAP_QUERYSTRING_REVVING = True
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SEND_FILE_MAX_AGE_DEFAULT = 43200


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + datadir + "/dev.sqlite"
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SEND_FILE_MAX_AGE_DEFAULT = 3  # 3 secs


class TestingConfig(DevelopmentConfig):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    DEBUG_TB_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = "postgresql:///localhost/example"
