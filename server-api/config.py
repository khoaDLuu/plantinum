import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['APP_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    ADMIN_USERNAME = os.environ['ADMIN_USERNAME']
    ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
