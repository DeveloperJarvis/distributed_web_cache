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
# distributed_web_cache MODULE
# --------------------------------------------------
"""
CLI Entry point for Distributed Web Cache
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import argparse
from core.distributed_cache import DistributedCache
from config.engine_config import CacheConfig
from exceptions.errors import CacheMissError


def parse_args():
    parser = argparse.ArgumentParser(
        description="Distributed Web Cache CLI"
    )
    parser.add_argument(
        "--key",
        type=str,
        help="Cache key to fetch/store",
    )
    parser.add_argument(
        "--value",
        type=str,
        default=None,
        help="Value to store in cache (if provided)",
    )
    parser.add_argument(
        "--policy",
        type=str,
        choices=["LRU", "LFU"],
        default="LRU",
        help="Eviction policy",
    )
    parser.add_argument(
        "--max-size",
        type=int,
        default=100,
        help="Maximum entries per cache node",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = CacheConfig(
        max_size=args.max_size,
        eviction_policy=args.policy,
    )
    cache = DistributedCache(config=config)

    if args.key and args.value is not None:
        cache.put(args.key, args.value.encode())
        print(f"✅ Stored key='{args.key}' with "
              f"value='{args.value}'")
    elif args.key:
        try:
            value = cache.get(args.key)
            print(f"🔹 Key='{args.key}' -> Value='{value}'")
        except CacheMissError:
            print(f"❌ Key '{args.key}' not found in cache")
    else:
        print("⚠️  Please provide a key with --key "
              "[and optionally --value]")


if __name__ == "__main__":
    main()
