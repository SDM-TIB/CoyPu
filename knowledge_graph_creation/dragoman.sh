#!/bin/bash

docker exec -it dragoman cp /knowledge_graph_creation/mapping_funcs/functions.py /app/Interpreter/

time curl localhost:6000/mapping_transformation/knowledge_graph_creation/configs/config_func.ini

# move translated functional mapping files into mapping folder
cp data/translated/*.ttl knowledge_graph_creation/mappings/


# python3 -m pip install dragoman-tool
# python3 -m Interpreter -c /path/to/config/file