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
# cache_controller MODULE
# --------------------------------------------------
"""
Cache controller for a single node.
Thread-safe cache operations.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import threading
from typing import Dict, Optional

from core.cache_node import CacheNode
from core.eviction import EvictionPolicy
from exceptions.errors import (
    CacheMissError,
    InvalidSizeError,
)
from utils.validators import validate_key


# --------------------------------------------------
# cache controller
# --------------------------------------------------
class CacheController:
    """
    Controls cache storage, eviction and access.
    """

    def __init__(
            self,
            max_size: int,
            eviction_policy: EvictionPolicy,
        ) -> None:
        if max_size <= 0:
            raise InvalidSizeError(
                "Cache size must be positive"
            )
        
        self._cache: Dict[str, CacheNode] = {}
        self._max_size = max_size
        self._current_size = 0
        self._eviction_policy = eviction_policy
        self._lock = threading.RLock()

    def get(self, key: str) -> CacheNode:
        validate_key(key)
        with self._lock:
            if key not in self._cache:
                raise CacheMissError(
                    f"Cache miss for key: {key}"
                )
            node = self._cache[key]
            node.touch()
            return node
    
    def put(self, key: str, value: bytes) -> None:
        validate_key(key)
        size = len(value)

        with self._lock:
            while self._current_size + size > self._max_size:
                evicted_key = self._eviction_policy.evict(
                    self._cache
                )
                self._remove(evicted_key)

            node = CacheNode(
                key=key,
                value=value,
                size=size,
            )
            node.touch()

            self._cache[key] = node
            self._current_size += size
    
    def _remove(self, key: str) -> None:
        node = self._cache.pop(key)
        self._current_size -= node.size
    
    def stats(self) -> str:
        with self._lock:
            return {
                "items": len(self._cache),
                "current_size": self._current_size,
                "max_size": self._max_size,
            }
