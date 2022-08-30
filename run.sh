#!/bin/bash

#load data sources
echo '##################### Uploading data on database ##################'
while true; do
    read -p "Do you wish to upload data on database?" yn
    case $yn in
        [Yy]* ) ./scripts/load_data.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done



# run Easy RML
# http://localhost:5000/

echo '##################### Runnning all docker services ##################'
while true; do
    read -p "Do you wish to run docker services?" yn
    case $yn in
        [Yy]* ) docker-compose down; docker-compose up -d; docker ps; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done


#dragoman
echo '##################### Execution of Dragoman for functions mappings ##################'
while true; do
    read -p "Do you wish to execute Dragoman tool for functions mappings?" yn
    case $yn in
        [Yy]* ) ./knowledge_graph_creation/dragoman.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done


#Sdm-rdfizer
echo '##################### Execution of Sdm-rdfizer for the transformation into RDF KG ##################'
while true; do
    read -p "Do you wish to execute Sdm-RDFfizer for the transformation into RDF KG?" yn
    case $yn in
        [Yy]* ) ./knowledge_graph_creation/sdm_rdfizer.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done


#graph-db

#valsparql
echo '##################### Validating class Instances ##################'
echo '##################### Open Link: http://localhost:5001/validate and provide correct path for shapes ##################'
echo '##################### Sparql endpoint Link: http://localhost:15000/sparql ##################'

#redash dashboard
# https://labs.tib.eu/sdm/coypu-endpoint/sparql

#general
#docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id

# for deleting files from remote side which are not on local side
#rsync -avP --delete generated_rdf_graph_data/*.nt node2:/data/coypu/sparql_endpoint/data_load

echo '##################### Setting up docker for CoyPU sparql endpoint##################'
echo '##################### Uploading RDF data files to triple store ##################'
while true; do
    read -p "Do you wish to upload RDF data files to triple store?" yn
    case $yn in
        [Yy]* ) echo '#####################Copying Graphs Data to Triple Store ##################'
                rsync -avP generated_rdf_graph_data/*.nt node2:/data/coypu/sparql_endpoint/data_load

                echo '##################### Backing-up Graphs Data on Triple Store ##################'
                rsync ssh 'cp /data/coypu/sparql_endpoint/data_load/*.nt /data/coypu/sparql_endpoint/data_backup/'
                echo '##################### Sparql endpoint setup ##################'
                scp ./knowledge_graph_creation/docker_command.sh node2://data/coypu/sparql_endpoint/;
                ssh node2 'cd /data/coypu/sparql_endpoint/ && ./docker_command.sh >out 2>error &';
                sleep 60s;
                ssh node2 'cat /data/coypu/sparql_endpoint/out || cat /data/coypu/sparql_endpoint/error &';
                break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done


