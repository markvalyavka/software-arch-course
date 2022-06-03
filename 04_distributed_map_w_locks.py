import sys
import time

import hazelcast


def no_locking(dist_map):
    dist_map.put_if_absent("1", 0)

    for i in range(1000):
        if i % 100 == 0:
            print(f"At {i}")
        val = dist_map.get("1")
        # sleep for 10 msec
        time.sleep(0.01)
        dist_map.put("1", val + 1)
    result = dist_map.get("1")
    print(f"Finished. Result = {result}")


def pessimistic_locking(dist_map):
    dist_map.put_if_absent("1", 0)

    for i in range(1000):
        try:
            dist_map.lock("1")
            val = dist_map.get("1")
            # sleep for 10 msec
            time.sleep(0.01)
            dist_map.put("1", val + 1)
        finally:
            dist_map.unlock("1")
    result = dist_map.get("1")
    print(f"Finished. Result = {result}")


def optimistic_locking(dist_map):
    dist_map.put_if_absent("1", 0)

    for i in range(1000):
        if i % 100 == 0:
            print(f"At {i}")
        while True:
            val = dist_map.get("1")
            new_val = val + 1
            # sleep for 10 msec
            time.sleep(0.01)
            if dist_map.replace_if_same("1", val, new_val):
                break
    result = dist_map.get("1")
    print(f"Finished. Result = {result}")

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="dev",
    )
    print("Connected.")
    # Create a Distributed Map in the cluster
    dist_map = client.get_map("my-distributed-map").blocking()
    locking_type = sys.argv[1]

    map_inserts_by_locking_type = {
        "nolock": no_locking,
        "pessimistic": pessimistic_locking,
        "optimistic": optimistic_locking,
    }
    map_inserts_by_locking_type[locking_type](dist_map)



