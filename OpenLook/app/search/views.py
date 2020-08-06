from flask import Flask, render_template, request
#import json
from . import search
from app.dao import data_access_object
import pysolr
import pandas as pd

@search.route("/search", methods=["GET", "POST"])

def search_str():
    rv = "" #rv: short for return value
    param = ""
    data = ""
    req = "GET"
    if request.method == "POST":
        print("post")
        req = "POST"
        if request.form["action"] == "Search":
            user_input = request.form["user_input"]
            rv = user_input
            param = request.form["options"] #this is in reference to <select name= "options"> in search.html
            if len(rv) < 2:
                data = ["Msg", "Blank input"]
            else:
                if param == "": #if not advanced search parameter is selected
                    try:
                        solr_data = data_access_object.DataAccess().search_string(rv)#, param) 
                        df = pd.DataFrame(solr_data) #create a dataframe with the result data
                        data = df.to_html(classes="table", justify='left', border=0, index=False) #rendering for the template
                    except Exception as e:
                        data = ["error", str(e)]
                elif param == "publisher": #if publisher is selected
                    try:
                        solr_data = data_access_object.DataAccess().group_by_publisher(rv)#, param) 
                        df = pd.DataFrame(solr_data) #create a dataframe with the result data
                        data = df.to_html(classes="table", justify='left', border=0, index=False) #rendering for the template
                    except Exception as e:
                        data = ["error", str(e)]
    #GET
    return render_template("search.html", rv=rv,req=req, data=data)#, param=param)