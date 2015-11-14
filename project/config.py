# project/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.abspath(os.path.join(os.path.dirname(basedir), 'data'))


class BaseConfig(object):
    """Base configuration."""
    APP_NAME = "Numerologia"
    SECRET_KEY = 'c+n8EzlJRyp55d3wZEKEYkhw7c97aagB+NDWb14Pd//DUvXoAeJxNQsck1'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    BOOTSTRAP_QUERYSTRING_REVVING = True
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + datadir + "/dev.sqlite"
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(DevelopmentConfig):
    """Testing configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:/'
    DEBUG_TB_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
