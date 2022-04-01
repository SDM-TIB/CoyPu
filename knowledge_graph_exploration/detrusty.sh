#!/bin/bash

docker exec -it detrusty python3 /DeTrusty/Scripts/create_rdfmts.py -s /DeTrusty/Config/endpoints.txt
docker exec -it detrusty /DeTrusty/Scripts/restart_workers.sh
curl -X POST localhost:5002/version
curl -X POST -d "query=SELECT ?s WHERE { ?s a  <https://schema.coypu.org/Disaster> } LIMIT 10" localhost:5002/sparql
# docker exec -it detrusty python3 /DeTrusty/runDeTrusty.py -q ./query.sparql -o True
