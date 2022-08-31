import requests
import pandas as pd
from io import StringIO
import base64
print(__package__)

# infai
id_or_user = 'coypu'
pass_or_secret = 'coypu'
url = 'http://coypu-fuseki.aksw.org/pdl/sparql'


query = """PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""


def get_auth():
        usr_pass = id_or_user + ':' + pass_or_secret
        auth =  "Basic {}".format(base64.b64encode(usr_pass.encode()).decode())
        return auth


def get_answer(url, query):
        url = url
        headers = {
                'Content-Type': 'application/sparql-query',
                'Accept': 'text/csv',  # text/html
                'Authorization': get_auth()}
        response = requests.request("POST", url, headers=headers, data=query)

        if response.status_code == 200:
            # print(response.text)
            return pd.read_csv(StringIO(str(response.content, 'utf-8')))
        return None
    

    
print (get_answer(url, query))
    


