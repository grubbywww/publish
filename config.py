import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You never to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[wangyj]'
    FLASKY_MAIL_SENDER = 'wangyj@easemob.com'
    FLASKY_ADMIN = 'wangyj@easemob.com'
    
    @staticmethod
    def init_app(app):
        pass
class ProductionConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://tests:Test1234@rds9xpp1484ti2j7r39f.mysql.rds.aliyuncs.com/tests'

iconfig = {
    'production': ProductionConfig,
    'default': ProductionConfig
}

