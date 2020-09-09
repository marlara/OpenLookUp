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
    filter_f = ""
    index = "" #trova un modo per evitare che bisogni sempre nominare prima le variabili
    req = "GET"
    if request.method == "POST":
        print("post")
        req = "POST"
        if request.form["action"] == "Search":
            user_input = request.form["user_input"]
            rv = user_input
            selection = request.form.getlist("selection") #multiple choice
            filter_f = request.form["filter_f"]
            param_group = request.form["grouping"] #this is in reference to <select name= "grouping"> in search.html
            if len(rv) < 2:
                data = "Nessun parametro per la ricerca!"
            else:
                if param_group: #if group by is selected
                    try:
                        solr_data = data_access_object.DataAccess().group_by(rv, param_group, filter_f)
                        df = pd.DataFrame(solr_data)
                        index = df.index
                        data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                    except Exception as e:
                        data = ["error", str(e)]
                else:
                    if selection: #if there are selected columns
                        try:
                            solr_data = data_access_object.DataAccess().select(rv, selection, filter_f) 
                            df = pd.DataFrame(solr_data) #create a dataframe with the result data
                            index = df.index
                            data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                        except Exception as e:
                            data = ["error", str(e)]
                    else: #simple search
                        try:
                            solr_data = data_access_object.DataAccess().search_string(rv, filter_f)  
                            df = pd.DataFrame(solr_data) #create a dataframe with the result data
                            index = df.index
                            data = df.to_html(classes=['table', 'linestab', 'table-striped','table-responsive'], justify='left', border=0, index=False) #rendering for the template
                        except Exception as e:
                            data = ["error", str(e)]                    
    #GET
    return render_template("search.html", rv=rv,req=req, data=data, param_group=param_group.replace("_db_map", ""), selection="; ".join(selection), data_count=len(index))