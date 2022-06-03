import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="dev",
    )
    print("Connected.")
    # Create a Distributed Map in the cluster
    dist_map = client.get_map("my-distributed-map").blocking()

    for i in range(1000):
        dist_map.put(f"{i}", i)
        # dist_map.delete(f"{i}")

    print("Finished")