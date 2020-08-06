import requests
import pysolr
import pandas as pd

class DataAccess:

    def __init__(self):
        self.solr = pysolr.Solr('https://search-2.medialibrary.it/solr/openmlol')
        pass

    def search_string(self, user_input):
        """Get just the results, plain (how to get more?)"""
        results = self.solr.search(user_input)
        #docs = results.docs
        return results

    def group_by_publisher(self, user_input):
        params = {
        'facet': 'on',
        'facet.field': 'publisher_db_map',
        'facet.query': user_input,
        }
        results = self.solr.search('*:*', **params)
        return results.facets
    """
    def get_docs_default(self, url_to_use):
        # r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*")
        url_full = url_to_use + "/newcore/select?q=*:*"
        r = requests.get(url_full)
        print("Solr status " + str(r.status_code))
        js = r.json()
        # print("Docs")
        li = js["response"]["docs"]
        # for l in li:
        #    print(l)
        return li

    def get_docs_max(self, url_to_use, default=10000):
        # r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*&rows=" + str(default))
        url_full = url_to_use + "/newcore/select?q=*:*&rows=" + str(default)
        r = requests.get(url_full)
        print("Solr status " + str(r.status_code))
        js = r.json()
        # print("Docs")
        li = js["response"]["docs"]
        # for l in li:
        #    print(l)
        return li
    """