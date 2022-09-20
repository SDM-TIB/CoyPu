#!/bin/bash

###### collecting metadata
# docker exec -it detrusty bash -c 'create_rdfmts.py -s /DeTrusty/Config/endpoints.txt'
docker exec -it detrusty bash -c 'create_rdfmts.py -s /DeTrusty/Config/endpoints.json -j'
docker exec -it detrusty restart_workers.sh 


####### Executing query ################
docker exec -it detrusty python3 /DeTrusty/runDeTrusty.py -q /DeTrusty/Query/query.sparql -o True

#execution
# sample example
curl -X POST localhost:5002/version
curl -X POST -d "query=SELECT ?s WHERE { ?s a <http://dbpedia.org/ontology/Scientist> } LIMIT 10" localhost:5002/sparql
curl -X POST -d "query=SELECT ?s WHERE { SERVICE <https://dbpedia.org/sparql> { ?s a <http://dbpedia.org/ontology/Scientist> }} LIMIT 10" -d "sparql1_1=True" localhost:5002/sparql

curl -X POST -d "query=PREFIX coy: <https://schema.coypu.org/global#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX time: <http://www.w3.org/2006/time#> 
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wds: <http://www.wikidata.org/entity/statement/>
PREFIX wdv: <http://www.wikidata.org/value/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX bd: <http://www.bigdata.com/rdf#>
PREFIX wb: <http://worldbank.org/>
PREFIX wbi: <http://worldbank.org/Indicator/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?year ?value ?disaster
WHERE {
    ?indicator a wb:AnnualIndicatorEntry .
    ?indicator wb:hasIndicator wbi:EN.ATM.CO2E.KT .
    ?indicator wb:hasCountry ?country .
    ?indicator owl:hasValue ?value .
    ?indicator time:year ?year .
    ?country   dc:identifier 'CHN' .

    ?disaster a coy:Disaster .
    ?disaster coy:hasLocation ?country_dis .
    ?disaster time:year ?year .
    ?country_dis coy:code-3166-1-alpha-3 'CHN' .
}
"

# https://l3s.coypu.org/ endpoint


