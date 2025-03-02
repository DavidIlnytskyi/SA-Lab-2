import hazelcast
import threading

if __name__ == "__main__":
    client = hazelcast.HazelcastClient()
    queue = client.get_queue("bounded-queue") 

    def produce():
        for i in range(100):
            queue.offer("value-" + str(i)).result()

    def consume(num_items):
        for _ in range(num_items): 
            head = queue.take().result()
            print(f"Consuming {head}")

    producer_thread = threading.Thread(target=produce)
    producer_thread.start()

    num_consumers = 2
    num_items_per_consumer = 100 // num_consumers  
    threads = []

    for _ in range(num_consumers):
        t = threading.Thread(target=consume, args=(num_items_per_consumer,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    producer_thread.join()
    client.shutdown()
