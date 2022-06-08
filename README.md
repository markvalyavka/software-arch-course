# software-arch-course


### watch demo on YT -> [https://youtu.be/6l2tjHNkuFg](https://www.youtube.com/watch?v=aRjiZe43jWg&ab_channel=%D0%9C%D0%B0%D1%80%D0%BA%D1%96%D1%8F%D0%BD%D0%92%D0%B0%D0%BB%D1%8F%D0%B2%D0%BA%D0%B0)

### Team:
- Mark Valyavka
- Andriy Bek


#### Run:
1. Run consul
```bash
docker run \
    -d \
    -p 8500:8500 \
    -p 8600:8600/udp \
    --name=badger \
    consul agent -server -ui -node=server-1 -bootstrap-expect=1 -client=0.0.0.0
```
2. Import preloaded cfg for Consul kv storage:
```bash
docker cp cfg.json badger:/cfg.json
docker exec badger consul kv import @/cfg.json
```

3. Run Hazelcast instances:
```bash
hz start
```

4. Run docker-compose
```bash
docker-compose -f docker/docker-compose.yml up --build
```

5. Go to http://localhost:5001/facade-service
