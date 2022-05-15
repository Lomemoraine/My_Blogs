class Config:
    
    random_quote='http://quotes.stormconsultancy.co.uk/random.json'
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