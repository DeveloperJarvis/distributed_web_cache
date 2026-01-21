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
# distributed_cache MODULE
# --------------------------------------------------
"""
Distributed cache abstraction.
Coordinates multiple cache nodes.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import Dict
import hashlib

from core.cache_controller import CacheController
from core.eviction import LRUEviction, LFUEviction
from config.engine_config import CacheConfig
from exceptions.errors import InvalidPolicyError


# --------------------------------------------------
# distributed cache
# --------------------------------------------------
class DistributedCache:
    """
    Distributed cache using sharding.
    """

    def __init__(self, config: CacheConfig) -> None:
        self._nodes: Dict[int, CacheController] = {}
        self._num_nodes = config.node_count

        eviction = self._create_eviction_policy(
            config.eviction_policy
        )

        for i in range(self._num_nodes):
            self._nodes[i] = CacheController(
                max_size=config.max_size,
                eviction_policy=eviction,
            )
    
    def _create_eviction_policy(self, policy: str):
        if policy == "LRU":
            return LRUEviction()
        if policy == "LFU":
            return LFUEviction()
        raise InvalidPolicyError(
            f"Unknown eviction policy: {policy}"
        )
    
    def _get_node(self, key: str) -> CacheController:
        """
        Hash-based sharding.
        """
        node_id = int(
            hashlib.md5(key.encode()).hexdigest(),
            16,
        ) % self._num_nodes
        return self._nodes[node_id]

    def get(self, key: str) -> bytes:
        node = self._get_node(key)
        return node.get(key).value
    
    def put(self, key: str, value: bytes) -> None:
        node = self._get_node(key)
        node.put(key, value)
    
    def stats(self) -> dict:
        return {
            f"node_{i}": node.stats()
            for i, node in self._nodes.items()
        }
