import os

from flask import Flask, render_template
from .search import search

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__) #for insance_relative_config see https://flask.palletsprojects.com/en/1.1.x/config/#instance-folders

    app.register_blueprint(search) #see Blueprints https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints

    # a simple page that says hello
    @app.route('/')
    def home():
        pagetitle = "HomePage - OpenLookUp"
        return render_template('base.html', mytitle=pagetitle)

    
    
    return app
