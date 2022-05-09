import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY= "purplesector"
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME="mosesmuta22@gmail.com"
    MAIL_PASSWORD="killa911G?"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}