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
# interactive_cli MODULE
# --------------------------------------------------
"""
Interactive CLI for Distributed Web Cache.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from config.engine_config import CacheConfig
from core.distributed_cache import DistributedCache
from exceptions.errors import CacheMissError


def main() -> None:
    config = CacheConfig(
        node_count=2,
        max_size=512,
        eviction_policy="LRU",
    )

    cache = DistributedCache(config)

    print("🌐 Distributed Web Cache CLI")
    print("Commands:")
    print(" PUT <key> <value>")
    print(" GET <key>")
    print(" STATS")
    print(" EXIT\n")

    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue

            if command.upper() == "EXIT":
                print("Goodbye 👋🏻")
                break

            if command.upper() == "STATS":
                for node, stats in cache.stats().items():
                    print(f"{node}: {stats}")
                continue

            parts = command.split(maxsplit=2)
            action = parts[0].upper()

            if action == "PUT" and len(parts) == 3:
                key, value = parts[1], parts[2]
                cache.put(key, value.encode())
                print(f"✔️ Stored [{key}]")
            
            elif action == "GET" and len(parts) == 2:
                key = parts[1]
                value = cache.get(key)
                print(f"✔️ {key} -> {value}")
            
            else:
                print("❌ Invalid command")
        
        except CacheMissError as e:
            print(f"⚠️  {e}")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
