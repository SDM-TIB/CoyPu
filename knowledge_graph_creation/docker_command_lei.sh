#!/bin/bash
#!/bin/bash

docker stop lei_endpoint

docker rm lei_endpoint

rm -rf /data/coypu/lei_endpoint/data/*.*

docker run -d --name lei_endpoint -v '/data/coypu/lei_endpoint/data_load/:/app/data' -v '/data/coypu/lei_endpoint/data/:/data' -p 11383:8890 --env NAMEDGRAPH=https://lei.coypu.org asakor/kglocal:latest

docker logs -f lei_endpoint

# port 11382:8890, 11383:8890 