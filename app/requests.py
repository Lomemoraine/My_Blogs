from urllib import response
import requests,json
from .models import Quote


random_quote = 'http://quotes.stormconsultancy.co.uk/random.json'
print(random_quote)

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(random_quote).json()
    quote = Quote(response.get("author"),response.get("quote"))
    return quote