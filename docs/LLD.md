## **Low-Level Design (LLD)** for a **Distributed Web Cache**

---

## **1. System Overview**

A **Distributed Web Cache** stores frequently accessed HTTP responses closer to the client to reduce latency and backend load. The system should support:

- **HTTP request caching** (GET requests primarily)
- **Eviction policies** (LRU, LFU)
- **Concurrency** for multiple clients
- **Distributed architecture** with multiple nodes
- **TTL (Time-to-Live)** for cache entries

---

## **2. Core Components**

### **2.1 Cache Node**

Each cache node stores a portion of the data in memory or disk and handles requests independently.

- **Responsibilities**
  - Store cache entries
  - Implement eviction policies
  - Handle concurrent read/write requests
  - Expire entries based on TTL

- **Data Structures**
  - **LRU:** `OrderedDict` or doubly linked list + hash map
  - **LFU:** Min-heap or frequency map + doubly linked list
  - **Hash map** for fast key lookup (URL → CacheEntry)

- **Concurrency Handling**
  - Use **thread locks** (mutex) or **read-write locks** to ensure consistency
  - Optional: **async I/O** for network-bound operations

---

### **2.2 Cache Entry**

Represents a single cached HTTP response.

- **Attributes**
  - `url` (string)
  - `response` (HTTP response body + headers)
  - `timestamp` (for TTL)
  - `frequency` (for LFU)
  - `last_accessed` (for LRU)
  - `ttl` (time-to-live)

---

### **2.3 Eviction Policies**

#### **2.3.1 LRU (Least Recently Used)**

- Evicts the cache entry that was **least recently accessed**
- **Data structures**:
  - Hash map for O(1) access
  - Doubly linked list to maintain usage order

- On cache hit → move node to the front
- On cache miss & full → evict tail node

#### **2.3.2 LFU (Least Frequently Used)**

- Evicts the cache entry with **lowest access frequency**
- **Data structures**:
  - Hash map for key → node
  - Frequency map: freq → doubly linked list of nodes

- On access → increment frequency and move node
- On eviction → remove from lowest frequency list

---

### **2.4 Cache Controller**

- Acts as the **entry point** for HTTP requests
- **Responsibilities**
  - Check cache for a request
  - Fetch from origin if cache miss
  - Insert response into cache
  - Choose eviction policy

- Can be implemented as a **singleton per node** or via a **distributed coordinator**

---

### **2.5 Cache Cluster / Distributed Layer**

- Multiple nodes form a cluster
- **Responsibilities**
  - Shard keys across nodes (consistent hashing)
  - Handle node failures
  - Optional replication for fault tolerance

- **Components**
  - **Hash ring** or **consistent hashing** to map URL → node
  - **Heartbeat mechanism** to monitor node health

---

## **3. Workflow (HTTP GET request)**

1. Client sends HTTP GET request
2. Cache controller checks **local cache**
   - If **hit**, return cached response
   - If **miss**, forward to origin server

3. On receiving response:
   - Normalize URL (optional)
   - Insert response into cache
   - Evict entries if memory limit exceeded

4. Update **metadata**
   - Last accessed (LRU)
   - Frequency (LFU)
   - Timestamp (TTL)

---

## **4. Concurrency Considerations**

- **Multiple clients** may read/write simultaneously
- **Locks**
  - **Fine-grained locks** per cache entry or per frequency bucket
  - **Global lock** only for critical operations (e.g., eviction)

- **Atomic operations** for frequency updates
- **Thread-safe data structures** or Python’s `collections` + `threading.Lock`

---

## **5. Optional Enhancements**

- **TTL eviction**: periodically clean expired entries
- **Async fetch**: non-blocking origin fetch using `asyncio`
- **Metrics**: hit/miss ratio, memory usage
- **Replication & Consistency**: master/slave nodes or quorum writes
- **Compression & serialization**: store large responses efficiently

---

## **6. High-Level Class Design (without code)**

```
CacheEntry
  - url
  - response
  - ttl
  - last_accessed
  - frequency

CacheNode
  - cache_map: dict(url → CacheEntry)
  - eviction_policy: LRU or LFU
  - max_size
  - insert(url, response)
  - get(url)
  - evict()

LRUManager
  - linked_list for usage
  - move_to_front()
  - remove_tail()

LFUManager
  - freq_map: dict(freq → list of CacheEntry)
  - increment_frequency(url)
  - remove_lowest_frequency()

CacheController
  - get(url)
  - put(url, response)
  - choose_eviction_policy()

DistributedCache
  - nodes: list(CacheNode)
  - consistent_hashing(url)
  - forward_request(url)
```

---

## **7. Key Design Decisions**

| Decision                            | Rationale                                       |
| ----------------------------------- | ----------------------------------------------- |
| LRU / LFU                           | Support common caching strategies               |
| In-memory + optional disk           | Fast lookups + persistence                      |
| Locking per bucket / node           | Reduce contention in multi-threaded environment |
| Consistent hashing for distribution | Avoid full rebalancing when nodes join/leave    |
| TTL per cache entry                 | Prevent stale data                              |
| Asynchronous origin fetch           | Minimize blocking client requests               |

---

✅ **LLD Summary:**

- The system is modular: **CacheEntry → CacheNode → CacheController → DistributedCache**
- Supports **LRU/LFU eviction**, TTL, concurrency, and distribution
- Can be implemented in Python using `dict`, `OrderedDict`, `threading`, and optionally `asyncio`
