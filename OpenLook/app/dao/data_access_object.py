import requests
import pysolr
import pandas as pd

class DataAccess:

    def __init__(self):
        self.solr = pysolr.Solr('https://search-2.medialibrary.it/solr/openmlol')
        pass

    def search_string(self, user_input):
        """Gets just 10000 results"""
        results = self.solr.search(user_input, rows=100)
        #docs = results.docs
        return results

    def group_by(self, user_input, param_group):
        results = self.solr.search(user_input, rows=100)
        docs = results.docs
        df = pd.DataFrame(docs)
        if "publisher" in param_group or "creator" in param_group:
            string_param = param_group.replace("_db_map", "") #to get the litteral value
        else:
            string_param = param_group.replace("_db_map", "_ss")
        new_df = df[[param_group, string_param, "id"]] #create new dataframe with just the desired values
        exploded = new_df.set_index(['id']).apply(pd.Series.explode).reset_index() #EXPLODE the listed values!! see https://stackoverflow.com/a/59330040/5102877
        group = exploded.dropna().groupby([param_group, string_param])["id"].count() #see https://realpython.com/pandas-groupby/
        return group.reset_index() #see https://stackoverflow.com/questions/51171737/passing-pandas-groupby-result-to-html-in-a-pretty-way
