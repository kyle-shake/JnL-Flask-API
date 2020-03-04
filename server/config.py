# backend/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
mysql_local_base = 'mysql+mysqldb://jacknlin_apiFetcher:56ePeaYu33E5pTV@localhost:3306/'
database_name = 'jacknlin_dbV2'

class BaseConfig:
    """Base Configuration."""
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'my_precious')
    #DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    #DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name + '_test'

class ProductionConfig(BaseConfig):
    """Production Configuration"""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jacknlin_apiFetcher:56ePeaYu33E5pTV@jlocalhost:3306/'