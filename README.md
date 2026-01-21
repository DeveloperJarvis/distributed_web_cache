# Distributed Web Cache

**Distributed Web Cache** is a Python library providing a high-performance HTTP caching layer with **eviction policies** such as **LRU (Least Recently Used)** and **LFU (Least Frequently Used)**. It is designed for low-latency web applications and supports **concurrent access**, **TTL-based cache expiration**, and **distributed deployment**.

---

## 🏃🏻‍♂️ How to run

```bash
# setup environment
python -m venv .env
# start the environment
.env\Scripts\activate   # Windows
# OR
source .env/bin/activate    # Linux/ Ubuntu

# run setup
pip install -e .
# setup for dev
pip install -e .[dev]

# run main
python main.py --key <key>
python main.py --key <key> --value <value>

# run examples
python -m examples.basic_cache
python -m examples.distributed_demo
python -m examples.interactive_cli
```

---

## 🧪 How to test

```bash
# make sure env is up
# setup is for dev
# run tests
pytest -v
```

---

## **Features**

- 🔹 **HTTP Request Caching**: Cache responses for frequently requested URLs
- 🔹 **Eviction Policies**: Supports both **LRU** and **LFU** for efficient memory management
- 🔹 **Concurrency-Safe**: Thread-safe operations for multiple clients
- 🔹 **TTL Support**: Automatic expiration of stale cache entries
- 🔹 **Distributed Architecture**: Multiple cache nodes with consistent hashing and optional replication
- 🔹 **Metrics & Logging**: Track cache hits, misses, and frequency distribution

---

## **Installation**

```bash
git clone https://github.com/DeveloperJarvis/distributed_web_cache.git
cd distributed_web_cache
python -m venv .env
source .env/bin/activate  # Linux / macOS
.env\Scripts\activate     # Windows
pip install -e .[dev]
```

---

## **Usage**

### **Basic Example**

```python
from distributed_web_cache import CacheController, CacheNode, EngineConfig

# Configure a cache node
node_config = EngineConfig(max_size=1000, eviction_policy="LRU")
node = CacheNode(config=node_config)

# Create a cache controller
cache = CacheController(nodes=[node])

# Cache an HTTP response
url = "https://example.com/api/data"
response = "<html>Data</html>"
cache.put(url, response)

# Retrieve cached response
cached_response = cache.get(url)
print(cached_response)
```

---

### **Eviction Policies**

- **LRU (Least Recently Used)**: Removes the least recently accessed entry when cache is full
- **LFU (Least Frequently Used)**: Removes the entry with the lowest access frequency when cache is full

---

### **Distributed Setup**

```python
from distributed_web_cache import DistributedCache, CacheNode, EngineConfig

# Create multiple nodes
nodes = [
    CacheNode(config=EngineConfig(max_size=500)),
    CacheNode(config=EngineConfig(max_size=500)),
]

# Initialize distributed cache
distributed_cache = DistributedCache(nodes=nodes)

# Fetch or cache data
url = "https://example.com/data"
data = distributed_cache.get(url)
if not data:
    data = "<html>Data from origin</html>"
    distributed_cache.put(url, data)
```

---

## **Concurrency Support**

- Thread-safe operations using locks
- Optional asynchronous fetch from origin servers using `asyncio`
- Designed to handle multiple simultaneous clients

---

## **Configuration**

| Parameter         | Description                                 | Default |
| ----------------- | ------------------------------------------- | ------- |
| `max_size`        | Maximum number of entries per cache node    | 1000    |
| `eviction_policy` | Eviction strategy: `"LRU"` or `"LFU"`       | LRU     |
| `ttl`             | Time-to-live for each cache entry (seconds) | None    |
| `replication`     | Number of replicas per cache entry          | 1       |

---

## **Project Structure**

```
distributed_web_cache/
│
├─ core/                # Core caching logic
│   ├─ cache_node.py
│   ├─ cache_controller.py
│   ├─ eviction.py
│   └─ distributed_cache.py
│
├─ storage/             # Storage layer for cache entries
│   └─ frequency_store.py
│
├─ utils/               # Helpers and utilities
│   ├─ logging.py
│   └─ validators.py
│
├─ exceptions/          # Custom exceptions
│   └─ errors.py
│
├─ examples/            # Example scripts
│
├─ tests/               # Unit tests
│
├─ main.py              # CLI entry point
└─ setup.py             # Package setup
```

---

## **Contributing**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a Pull Request

---

## **License**

This project is licensed under the **GNU General Public License v3 or later (GPL-3.0-or-later)**.

---

## **Contact**

- **Author:** Developer Jarvis (Pen Name)
- **GitHub:** [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)
