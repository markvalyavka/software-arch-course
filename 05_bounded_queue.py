import sys
import time

import hazelcast

# 0. Added in hazelcast.xml
# <queue name="queue">
#     <max-size>10</max-size>
# </queue>


def run_producer(q):
    for i in range(50):
        q.put(i)
        print(f"Producing {i}")
        time.sleep(1)
    q.put(-1)
    print("Producer finished.")


def run_consumer(q):
    while True:
        val = q.take()
        print(f"consumed: {val}")
        if val == -1:
            break
        time.sleep(0.5)
    print("Consumer finished.")


if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="dev",
    )
    print("Connected.")
    q = client.get_queue("my-queue").blocking()

    run_as = sys.argv[1]
    rus_as_by_func = {
        "producer": run_producer,
        "consumer": run_consumer,
    }
    rus_as_by_func[run_as](q)
