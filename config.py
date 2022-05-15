class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorraine:gift1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    pass
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    '''
    Dev config class to be used during development process
    '''
    DEBUG = True
    
      

config_options = {
'development':DevConfig,
'production':ProdConfig

}