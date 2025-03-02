# SA-Lab-2

## Docker setup

**Create network**
```
docker network create --subnet=172.18.0.0/16 hazelcast-network
```

**Container 1**
```
docker run --rm -v "$(pwd)"/hazelcast-docker.xml:/opt/hazelcast/hazelcast-docker.xml \
  -e HAZELCAST_CONFIG=hazelcast-docker.xml \
  --network hazelcast-network \
  --ip 172.18.0.10 \
  --name member1 \
  -p 5701:5701 \
  hazelcast/hazelcast:latest
```


**Container 2**
```
docker run --rm -v "$(pwd)"/hazelcast-docker.xml:/opt/hazelcast/hazelcast-docker.xml \
  -e HAZELCAST_CONFIG=hazelcast-docker.xml \
  --network hazelcast-network \
  --ip 172.18.0.11 \
  --name member2 \
  -p 5702:5701 \
  hazelcast/hazelcast:latest
```

**Container 3**
```
docker run --rm -v "$(pwd)"/hazelcast-docker.xml:/opt/hazelcast/hazelcast-docker.xml \
  -e HAZELCAST_CONFIG=hazelcast-docker.xml \
  --network hazelcast-network \
  --ip 172.18.0.12 \
  --name member3 \
  -p 5703:5701 \
  hazelcast/hazelcast:latest
```