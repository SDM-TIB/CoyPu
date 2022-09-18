import requests
from .credentials import *
from .functions import *
import pandas as pd
from io import StringIO
print(__package__)
from os.path import join

class Query:
    def __init__(self, url, id_or_user, pass_or_secret):
        self.url = url
        self.id_or_user = id_or_user
        self.pass_or_secret = pass_or_secret
        self.auth = None
    
    @get_auth
    def get_answer(self, query, query_desc, save_path, ret_format='text/csv'):
        pass
    
    def set_headers(self, ret_format='text/csv'):
        headers = {
                'Content-Type': 'application/sparql-query',
                'Accept': ret_format}  # text/html
                
        if self.auth:
            headers['Authorization']= self.auth
        return headers
    

class CMEMCQuery(Query):
    def __init__(self, url, id_or_user, pass_or_secret):
        super().__init__(url, id_or_user, pass_or_secret)
    
    @timer
    @get_auth_os2
    def get_answer(self, query, query_desc, save_path, ret_format='text/csv'):
        url = self.url + "/dataplatform/proxy/default/sparql"
        headers = self.set_headers(ret_format)
        
        response = requests.request("POST", url, headers=headers, data=query, stream=True)

        if response.status_code == 200:
            print("Passed Query: {}".format(query_desc))
            filename = '_'.join(query_desc.split(' '))
            with open(join(save_path, filename+'.raw'), 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)
            # return pd.read_csv(StringIO(str(response.content, 'utf-8')))
            return True
        print("Failed Query: {} Error:{}".format(query_desc, response.content))
        return False


class FusekiQuery(Query):
    def __init__(self, url, id_or_user, pass_or_secret):
        super().__init__(url, id_or_user, pass_or_secret)

    @timer
    @get_auth_basic
    def get_answer(self, query, query_desc, save_path, ret_format='text/csv'):
        url = self.url
        headers = self.set_headers(ret_format)
        response = requests.request("POST", url, headers=headers, data=query, stream=True)

        if response.status_code == 200:
            print("Passed Query: {}".format(query_desc))
            filename = '_'.join(query_desc.split(' '))
            with open(join(save_path, filename+'.csv'), 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)
            # return pd.read_csv(StringIO(str(response.content, 'utf-8')))
            return True
        print("Failed Query: {} Error:{}".format(query_desc, response.content))
        return False

class FDQuery(Query):
    def __init__(self, url, id_or_user=None, pass_or_secret=None):
        super().__init__(url, id_or_user, pass_or_secret)
    
    def set_headers(self, ret_format='text/csv'):
            headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                      }
            return headers

    @timer
    def get_answer(self, query, query_desc, save_path, ret_format='text/csv', sparql1_1=False):
        url = self.url
        headers = self.set_headers(ret_format)
        if sparql1_1==True:
            response = requests.request("POST", url, headers=headers, data="query="+query+"&sparql1_1=True")
        else:
            response = requests.request("POST", url, headers=headers, data="""query="""+query)
        
        if response.status_code == 200:
            print("Passed Query: {}".format(query_desc))
            filename = '_'.join(query_desc.split(' '))
            with open(join(save_path, filename+'.json'), 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)
            return True
        print("Failed Query: {} Error:{}".format(query_desc, response.content))
        return False
        

def main(client_url='', client_id='', client_secret='',
         query="""SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""):
    
    cmemc_query = CMEMCQuery(client_url, client_id, client_secret)
    print(cmemc_query.get_answer(query))
    
    
#    fuseki_query = FusekiQuery(fuseki_endpoint, fuseki_user_infai, fuseki_pw_infai)
#    print (fuseki_query.get_answer(query))
    

if __name__ == "__main__":
    
    query = """PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""
        
    main(client_url_tib, client_id_tib,
         client_secret_tib, query)
    main (client_url_imp, client_id_imp,
         client_secret_imp, query)
    main(client_url_infai, client_id_infai,
         client_secret_infai, query)
