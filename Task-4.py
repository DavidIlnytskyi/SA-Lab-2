import hazelcast
import threading

THREAD_NUMBER: int = 3
threads = []


def increment_value():
    print("Starting client...")
    client = hazelcast.HazelcastClient(
        cluster_members=[
            "172.18.0.10:5701",
            "172.18.0.11:5701",
            "172.18.0.12:5701"
        ]
    )
    distributed_map = client.get_map("my-distributed-map").blocking()

    for _ in range(10000):
        value = int(distributed_map.get("key"))
        value += 1
        distributed_map.put("key", value)

    print("Client finished incrementing.")
    client.shutdown()

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

    print(f"Starting value of \"key\": {distributed_map.get('key')}")

    for _ in range(THREAD_NUMBER):
        t = threading.Thread(target=increment_value)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    client = hazelcast.HazelcastClient(
        cluster_members=[
            "172.18.0.10:5701",
            "172.18.0.11:5701",
            "172.18.0.12:5701"
        ]
    )
    final_value = distributed_map.get("key")
    print(f"Final value of \"key\": {final_value}")

    client.shutdown()
