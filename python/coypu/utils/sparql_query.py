import requests
import credentials
import pandas as pd
from io import StringIO
print(__package__)


def get_token(client_url, client_id, client_secret):
    url = client_url + "/auth/realms/cmem/protocol/openid-connect/token"
    payload = 'grant_type=client_credentials&client_id={}&client_secret={}'\
              .format(client_id, client_secret)

    headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()['access_token']
    return None


def get_answer(client_url, token, query):
    url = client_url + "/dataplatform/proxy/default/sparql"
    payload = query
    headers = {
            'Content-Type': 'application/sparql-query',
            'Accept': 'text/csv',  # text/html
            'Authorization': 'Bearer ' + token}
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        # print(response.text)
        return pd.read_csv(StringIO(str(response.content, 'utf-8')))
    return None


def main(client_url='', client_id='', client_secret='',
         query="""SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""):
    query = """PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?s ?o WHERE{?s a ?o.} LIMIT 10"""

    token = get_token(client_url, client_id, client_secret)
    if token is not None:
        print(get_answer(client_url, token, query))
    else:
        print('No token generated')


if __name__ == "__main__":
    main(credentials.client_url_tib, credentials.client_id_tib,
         credentials.client_secret_tib)
