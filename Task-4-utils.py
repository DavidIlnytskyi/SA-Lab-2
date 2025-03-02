import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_members=[
            "172.18.0.10:5701",
            "172.18.0.11:5701",
            "172.18.0.12:5701"
        ]
    )
    distributed_map = client.get_map("my-distributed-map").blocking()
    
    distributed_map.put("key", 0)

    client.shutdown()
