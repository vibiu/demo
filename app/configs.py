from os.path import abspath, join


def datapath(path):
    return abspath(join('data', path))


class Default:
    DEBUG = True
    DEBUG_LOG = datapath('debug.log')
    ERROR_LOG = datapath('error.log')
    SECRET_KEY = 'vibiu_s_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + datapath('sqlite.db')


class Product(Default):
    DEBUG = False


class Testing(Default):
    TESTING = True

configs = {
    'defautl': Default,
    'product': Product,
    'testing': Testing
}
