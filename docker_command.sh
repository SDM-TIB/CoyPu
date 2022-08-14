#!/bin/bash
#!/bin/bash

docker stop coypu_endpoint

docker rm coypu_endpoint

rm -rf /data/coypu/sparql_endpoint/data/*.*

docker run -d --name coypu_endpoint -v '/data/coypu/sparql_endpoint/data_load/:/app/data' -v '/data/coypu/sparql_endpoint/data/:/data' -p 41110:8890 --env NAMEDGRAPH=https://l3s.coypu.org asakor/kglocal:latest

docker logs -f coypu_endpoint