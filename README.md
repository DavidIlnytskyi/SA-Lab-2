# SA-Lab-2

## 1-2 Docker setup

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

**Managment center:**
```
docker run --rm --network hazelcast-network -p 8080:8080 hazelcast/management-center 
```


## 3. Distributed Map

**Python code:**\
![Task-3-Code](./images/Task-3-Code.png)


**Output:**\
![Task-3-cmd](./images/Task-3-cmd.png)

**Managment center statistics::**\
![Task-3-Linex](./images/Task-3-Data-1-Lines.png)
![Task-3-Plots](./images/Task-3-Data-1-Plots.png)

### Clusters removing(`kill -9 <pid>`):
- 1 cluster:   
![Task-3-Lines](./images/Task-3-Data-Kill-One-Lines.png)
![Task-3-Plots](./images/Task-3-Data-Kill-One-Plots.png)
    - no data loss
    ![Task-3-Data-Loss](./images/Task-3-Data-Kill-One-No-Loss.png)

- 2 clusters sequentially:
![Task-3-Lines](./images/Task-3-Data-Kill-Two-Seq-Lines.png)
![Task-3-Plots](./images/Task-3-Data-Kill-Two-Seq-Plots.png)
    - data loss
    ![Task-3-Data-Loss](./images/Task-3-Data-Kill-Two-Data-Loss.png)

- 2 clusters simultaneously:
![Task-3-Lines](./images/Task-3-Data-Kill-Two-Simul-Lines.png)
![Task-3-Plots](./images/Task-3-Data-Kill-Two-Simul-Plots.png)
    - data loss
    ![Task-3-Data-Loss](./images/Task-3-Data-Kill-Two-Simul-Data-Loss.png)

**Так, втрата даних є.**

Шляхи уникнення втрати даних:
- use back-up copies
- enable persistance

## 4. Distributed Map without locks


![Task-4-results](./images/Task-4-Results.png)


## 5. Distributed map with pessimistic locks 
![Task-5-results](./images/Task-5-Results.png)

## 6. Distributed map with optimistic locks
![Task-6-results](./images/Task-6-Results.png)

## 7. Compare results
**Без блокувань спостерігаються втрати даних.\
Оптимістичний та песимістичний блокування працюють приблизно однаково, з незначною перевагою в сторону песимістичного.**

## 8. Bounded Queue
**Створити Bounded-Queue**

**Заранити 1 producer  і 2 consumer's**
![Task-8-Results](./images/Task-8-Results.png)
Значення вичитуються послідовно.