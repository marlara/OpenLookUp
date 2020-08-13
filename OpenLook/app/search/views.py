from flask import Flask, render_template, request
#import json
from . import search
from app.dao import data_access_object
import pysolr
import pandas as pd

@search.route("/search", methods=["GET", "POST"])

def search_str():
    rv = "" #rv: short for return value
    param_group = ""
    selection = ""
    data = ""
    req = "GET"
    if request.method == "POST":
        print("post")
        req = "POST"
        if request.form["action"] == "Search":
            user_input = request.form["user_input"]
            rv = user_input
            selection = request.form.getlist("selection") #multiple choice
            param_group = request.form["grouping"] #this is in reference to <select name= "grouping"> in search.html
            if len(rv) < 2:
                data = "Nessun parametro per la ricerca"
            else:
                if param_group == "": #if group by is not selected
                    if selection == "":
                        try:
                            solr_data = data_access_object.DataAccess().search_string(rv) 
                            df = pd.DataFrame(solr_data) #create a dataframe with the result data
                            data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                        except Exception as e:
                            data = ["error", str(e)]
                    else:
                        try:
                            solr_data = data_access_object.DataAccess().select(rv, selection) 
                            df = pd.DataFrame(solr_data) #create a dataframe with the result data
                            data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                        except Exception as e:
                            data = ["error", str(e)]
                else: #if param is selected
                    try:
                        solr_data = data_access_object.DataAccess().group_by(rv, param_group)
                        df = pd.DataFrame(solr_data)
                        data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                    except Exception as e:
                        data = ["error", str(e)]
    #GET
    return render_template("search.html", rv=rv,req=req, data=data)#, param_group=param_group)