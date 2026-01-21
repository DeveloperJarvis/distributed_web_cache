# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Distributed Web Cache Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Distributed Web Cache - HTTP caching layer with eviction policies (LRU/LFU)
#                   Skills: networking, caching algorithms, concurrency
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# distributed_demo MODULE
# --------------------------------------------------
"""
Demonstration of distributed caching across nodes.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from config.engine_config import CacheConfig
from core.distributed_cache import DistributedCache


def main() -> None:
    config = CacheConfig(
        node_count=3,
        max_size=256,
        eviction_policy="LFU",
    )

    cache = DistributedCache(config)

    keys = [
        "user:1",
        "user:2",
        "session:1",
        "product:9",
        "order:42",
    ]

    print("🔹 Inserting keys into distributed cache")
    for key in keys:
        cache.put(key, key.encode())
    
    print("\n🔹 Access pattern (to affect LFU)")
    cache.get("user:1")
    cache.get("user:1")
    cache.get("session:1")

    print("\n📊 Distributed Cache Stats:")
    for node, stats in cache.stats().items():
        print(f"{node}: {stats}")


if __name__ == "__main__":
    main()
