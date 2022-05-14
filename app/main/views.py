from flask import render_template,request,redirect,url_for,abort
from . import main
#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home _ Welcome to family news Hub"
    return render_template('index.html',title = title)
