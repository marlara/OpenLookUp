
from flask import Flask, render_template, request
import json

from . import home

@home.route("/")
def index():
    
    return render_template("index.html")

@home.route("/about")
def about():
    return render_template("about.html")