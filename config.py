import os
class Config:
    SECRET_KEY ='lorraine'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    pass
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
    pass


class DevConfig(Config):
    '''
    Dev config class to be used during development process
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorraine:gift1234@localhost/blog'
    # DEBUG = True
    
class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorraine:gift1234@localhost/blog_test'
    pass
      

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}