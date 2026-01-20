## Project Structure

```
distributed_web_cache/
│
├─ core/                     # Core caching logic
│   ├─ cache_node.py          # Single cache node, stores entries and applies eviction policy
│   ├─ cache_controller.py    # Manages multiple nodes, central interface for cache operations
│   ├─ eviction.py            # Eviction policies (LRU, LFU) implementations
│   └─ distributed_cache.py   # Distributed cache layer with node mapping, replication, and routing
│
├─ storage/                  # Storage abstractions for cache entries
│   └─ frequency_store.py     # Maintains frequency counts for LFU eviction
│
├─ utils/                     # Utility helpers
│   ├─ logging.py             # Configured logging
│   ├─ validators.py          # Input validation helpers
│   └─ normalizer.py          # Optional: normalize keys/URLs
│
├─ exceptions/                # Custom exceptions
│   └─ errors.py              # Cache-specific exceptions (CacheError, NodeError, EvictionError)
│
├─ config/                    # Configuration layer
│   ├─ defaults.py            # Default settings (max_size, TTL, eviction policy)
│   └─ engine_config.py       # Config dataclasses for nodes & distributed cache
│
├─ examples/                  # Example scripts demonstrating usage
│   ├─ basic_cache.py
│   ├─ distributed_demo.py
│   └─ interactive_cli.py
│
├─ tests/                     # Unit tests
│   ├─ test_cache_node.py
│   ├─ test_distributed_cache.py
│   ├─ test_eviction.py
│   ├─ test_frequency_store.py
│   └─ test_utils.py
│
├─ main.py                    # CLI entry point for interactive caching
├─ README.md                  # Project documentation
├─ setup.py                   # Package setup & dependencies
└─ pyproject.toml             # Build system configuration
```

### **Highlights of this structure**

1. **`core/`** handles the main logic: caching, eviction, and distributed coordination.
2. **`storage/`** abstracts data structures for frequency tracking (LFU) and potentially persistent storage.
3. **`utils/`** contains reusable helpers (logging, validation, normalization).
4. **`exceptions/`** defines clear exception classes for cache operations.
5. **`config/`** centralizes default parameters and node/distributed configuration.
6. **`examples/`** demonstrates practical usage scenarios (local caching, distributed mode, CLI).
7. **`tests/`** ensures each component (eviction, node, distributed cache) is fully tested.
