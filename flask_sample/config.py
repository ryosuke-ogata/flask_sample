# config.py
class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGO_DBNAME = 'flask_sample'
    MONGO_MAX_POOL_SIZE = 5

class ProductionConfig(Config):
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
