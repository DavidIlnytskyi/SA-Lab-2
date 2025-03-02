import hazelcast
import threading
import time

THREAD_NUMBER: int = 3
threads = []
key = "key"


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
        success = False
        while(success != True):
            current_value = distributed_map.get(key)
            updated_value = current_value + 1
            success = distributed_map.replace_if_same(key, current_value, updated_value)

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
    
    distributed_map.put(key, 0)

    print(f"Starting value of {key}: {distributed_map.get('key')}")

    start_time = time.time()

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
    final_value = distributed_map.get(key)
    print(f"Final value of {key}: {final_value}")
    print("Used time: ", (time.time() - start_time), " seconds.") 

    client.shutdown()
