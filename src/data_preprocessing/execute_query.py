import requests
import pandas as pd
from io import StringIO

# change url
client_url = 'https://tib.coypu.org'
client_id='cmem-service-account'
# provide client_secret
client_secret='y3mOi5ENXbJrrEJXCIZAh9Q2OJ4YPrLF'   # format:'y3mOi5ENXbJrrEJXCIZAh9Q2OJ4Y'


if client_secret=='':
      print ('define client secret code')
      exit()
      
      

query = """PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
         SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""


def get_token():
      url = client_url + "/auth/realms/cmem/protocol/openid-connect/token"
      payload='grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id, client_secret)
      
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      
      if response.status_code==200:
        return response.json()['access_token']
      return None



def get_answer(token, query):
      
      url = client_url + "/dataplatform/proxy/default/sparql"

      payload = query
      
      headers = {
        'Content-Type': 'application/sparql-query',
        'Accept': 'text/csv', #'text/html',
        'Authorization': 'Bearer ' + token}

      response = requests.request("POST", url, headers=headers, data=payload)
      if response.status_code==200:
            # print(response.text)
            return pd.read_csv(StringIO(str(response.content, 'utf-8')))
      return None
          
      



token = get_token()

if token is not None:
      print(get_answer(token, query))
else:
      print('No token generated')



