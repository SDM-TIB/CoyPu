#!/bin/bash

# time python -m rdfizer -c ./knowledge_graph_creation/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph_creation/configs/config.ini

time docker exec -it semantic_enrichment python3 -m rdfizer -c /knowledge_graph_creation/configs/config.ini