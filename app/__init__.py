from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .search import search as search_blueprint
app.register_blueprint(search_blueprint)