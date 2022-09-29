""" Python Script to execute SPARQL queries on WorldBank Endpoint 
"""


import requests
from urllib.parse import urlencode, quote


# Url to access UI interface to query worldbank dataset
url = "https://labs.tib.eu/sdm/worldbank_endpoint/sparql"


query =("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX time: <http://www.w3.org/2006/time#> 
PREFIX wb: <http://worldbank.org/>
PREFIX wbi: <http://worldbank.org/Indicator/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT DISTINCT ?wbi ?label ?identfier ?topic ?note
WHERE
{
    ?wbi a wb:Indicator.
    Optional {?wbi rdfs:label ?label}
    Optional {?wbi wb:hasTopic ?topic}
    Optional {?wbi dc:identifier ?identfier}
    Optional {?wbi skos:note ?note}
}""")


payload='default-graph-uri=&query={}'.format(quote(query))

headers = {
  'Accept': 'text/csv',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
