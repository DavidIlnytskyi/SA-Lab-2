import hazelcast

client = hazelcast.HazelcastClient(
    cluster_members=[
        "172.18.0.10:5701",
        "172.18.0.11:5701",
        "172.18.0.12:5701"
    ]
)

distributed_map = client.get_map("my-distributed-map").blocking()

print("Reading values...")

for idx in range(1001):
    # distributed_map.put(idx, f"Value_{idx}")
    print(distributed_map.get(idx))   
# distributed_map.remove(idx)
# print(distributed_map.key_set())

print("Readed successfully...")


client.shutdown()
