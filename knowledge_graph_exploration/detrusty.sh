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


# https://l3s.coypu.org/ endpoint


