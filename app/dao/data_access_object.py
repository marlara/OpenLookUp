import requests
import pysolr
import pandas as pd

class DataAccess:

    def __init__(self):
        self.solr = pysolr.Solr('https://search-2.medialibrary.it/solr/openmlol')
        pass

    def search_string(self, user_input, filter_f):
        """Gets just 100 results"""
        if filter_f == "": #if no field filtered
            results = self.solr.search(user_input, rows=100)
        else:
            field = filter_f
            query = f"{field}:{user_input}"
            results = self.solr.search(query, rows = 100)
        docs = results.docs
        df = pd.DataFrame(docs)
        df = df[['id','title', 'publisher', 'typology', 'creator_sort', 'viaf', 'viafname', 'wikidata', 'collection_ss', 'language_ss', 'license_ss', 'subject_ss', 'tag_ss', 'description', 'schoolgrade_ss']]
        return df

    def select(self, user_input, selection, filter_f):
        """Gets just 100 results"""
        if filter_f == "": #if no field filtered
            results = self.solr.search(user_input, rows=100)
        else:
            field = filter_f
            query = f"{field}:{user_input}"
            results = self.solr.search(query, rows = 100)
        docs = results.docs
        df = pd.DataFrame(docs)
        df = df[['id'] + selection]
        df['scheda'] = "https://medialibrary.it/media/schedaopen.aspx?id="+df['id']
        return df

    def group_by(self, user_input, param_group, filter_f):
        if filter_f == "": #if no field filtered
            results = self.solr.search(user_input, rows=10000)
        else:
            field = filter_f
            query = f"{field}:{user_input}"
            results = self.solr.search(query, rows=10000)
        docs = results.docs
        df = pd.DataFrame(docs)
        if "publisher" in param_group or "creator" in param_group or "typology" in param_group:
            string_param = param_group.replace("_db_map", "") #to get the litteral value
        else:
            string_param = param_group.replace("_db_map", "_ss")
        new_df = df[[param_group, string_param, "id"]] #create new dataframe with just the desired values
        new_df.rename(columns={'id':'Numero di risorse'}, inplace=True) #rename the column for better understanding
        exploded = new_df.set_index(['Numero di risorse']).apply(pd.Series.explode).reset_index() #EXPLODE the listed values!! see https://stackoverflow.com/a/59330040/5102877
        make_group = exploded.groupby([param_group, string_param])["Numero di risorse"].count() #see https://realpython.com/pandas-groupby/
        return make_group.reset_index() #see https://stackoverflow.com/questions/51171737/passing-pandas-groupby-result-to-html-in-a-pretty-way
