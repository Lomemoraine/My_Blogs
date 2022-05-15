from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quote
#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote()
    title = "Home _ Welcome to family news Hub"
    return render_template('index.html',title = title,quote=quote)
