import os

  
class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:dclxvi@127.0.0.1:5432/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgresql://ckrctazlhrjoep:bb8d90660e579b908322468873f6fb38b5a298677ee47e80e87bf2d4f0c59260@ec2-44-196-223-128.compute-1.amazonaws.com:5432/dc1f0nupgurpbr"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:dclxvi@127.0.0.1:5432/pitch'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}