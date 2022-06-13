#!/bin/bash

# Copy nedpoints file inside container
# docker exec -it detrusty cp /DeTrusty/Config/endpoints.txt /DeTrusty/Config/endpoints.txt

# docker exec -it detrusty python3 /DeTrusty/Scripts/create_rdfmts.py -s /DeTrusty/Config/endpoints.txt
# docker exec -it detrusty /DeTrusty/Scripts/restart_workers.sh

#execution
#curl -X POST localhost:5002/version
# curl -X POST -d "query=SELECT ?s ?p WHERE { GRAPH <https://l3s.coypu.org/> {?s a  ?p} } LIMIT 10" localhost:5002/sparql
#curl -X POST -d "query=SELECT ?s ?p WHERE { ?s a  ?p} LIMIT 500" localhost:5002/sparql
# curl -X POST -d  "query=SELECT * FROM <https://l3s.coypu.org/> WHERE {?s a  ?p} LIMIT 2" localhost:5002/sparql
# curl -X POST -d "query=SELECT ?s WHERE { SERVICE <https://dbpedia.org/sparql> { ?s a <http://dbpedia.org/ontology/Scientist> }} LIMIT 10" -d "sparql1_1=True" localhost:5002/sparql

####### Executing query ################
docker exec -it detrusty python3 /DeTrusty/runDeTrusty.py -q /DeTrusty/Query/query.sparql -o True
