import os

class Config(object):
    # Parent configuration class
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    # Development configuration
    DEBUG = True

class TestingConfig(Config):
    # Testing configuration, with test_db
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'postgresql://localhost/test_db'

class StagingConfig(Config):
    #Staging configuration
    DEBUG = True

class ProductionConfig(Config):
    # Production configuration
    DEBUG = False
    TESTING = False

app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production': ProductionConfig,
}
