import requests
from credentials import *
import pandas as pd
from io import StringIO
import base64
print(__package__)

class Query:
    def __init__(self, url, id_or_user, pass_or_secret):
        self.url = url
        self.id_or_user = id_or_user
        self.pass_or_secret = pass_or_secret
        self.get_auth_()
        
    def get_auth_(self):
        pass
    
    def get_answer(self, query, re_format='text/csv'):
        pass
        
    
class CMEMCQuery(Query):
    def __init__(self, url, id_or_user, pass_or_secret):
        super().__init__(url, id_or_user, pass_or_secret)
        
    def get_auth_(self):
        url = self.url + "/auth/realms/cmem/protocol/openid-connect/token"
        payload = 'grant_type=client_credentials&client_id={}&client_secret={}'\
                .format(self.id_or_user, self.pass_or_secret)

        headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                  }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            self.auth = 'Bearer ' + response.json()['access_token']
        return None
    
    def get_answer(self, query, re_format='text/csv'):
        url = self.url + "/dataplatform/proxy/default/sparql"
        headers = {
                'Content-Type': 'application/sparql-query',
                'Accept': 'text/csv',  # text/html
                'Authorization': self.auth}
        
        response = requests.request("POST", url, headers=headers, data=query)

        if response.status_code == 200:
            # print(response.text)
            return pd.read_csv(StringIO(str(response.content, 'utf-8')))
        return None


class FusekiQuery(Query):
    def __init__(self, url, id_or_user, pass_or_secret):
        super().__init__(url, id_or_user, pass_or_secret)
    
    
    def get_auth_(self):
        usr_pass = self.id_or_user + ':' + self.pass_or_secret
        self.auth =  "Basic {}".format(base64.b64encode(usr_pass.encode()).decode())
        return None


    def get_answer(self, query, re_format='text/csv'):
        url = self.url
        headers = {
                'Content-Type': 'application/sparql-query',
                'Accept': re_format,  # text/html
                'Authorization': self.auth}
        response = requests.request("POST", url, headers=headers, data=query)

        if response.status_code == 200:
            # print(response.text)
            return pd.read_csv(StringIO(str(response.content, 'utf-8')))
        return None


def main(client_url='', client_id='', client_secret='',
         query="""SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""):
    query = """PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""
    
    cmemc_query = CMEMCQuery(client_url, client_id, client_secret)
    print(cmemc_query.get_answer(query))
    
    fuseki_query = FusekiQuery(fuseki_endpoint, fuseki_user_infai, fuseki_pw_infai)
    print (fuseki_query.get_answer(query))
    

if __name__ == "__main__":
    main(client_url_tib, client_id_tib,
         client_secret_tib)
