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
# engine_config MODULE
# --------------------------------------------------
"""
Cache configuration module
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from dataclasses import dataclass, field
from config.defaults import (
    DEFAULT_MAX_SIZE,
    DEFAULT_EVICTION_POLICY,
    DEFAULT_TTL,
    DEFAULT_NODE_COUNT,
)
from exceptions.errors import InvalidPolicyError


# --------------------------------------------------
# imports
# --------------------------------------------------
@dataclass(frozen=True)
class CacheConfig:
    """
    Configuration object for Distributed Web Cache.
    Attributes:
        max_size (int): Max entries per node
        eviction_policy (str): Eviction strategy ("LRU" or "LFU")
        ttl (int): Time-to-live for cache entries in seconds
        node_count (int): Number of cache nodes
    """
    max_size: int = DEFAULT_MAX_SIZE
    eviction_policy: str = DEFAULT_EVICTION_POLICY
    ttl: int=DEFAULT_TTL
    node_count: int = DEFAULT_NODE_COUNT

    def __post_init__(self):
        if self.max_size <= 0:
            raise ValueError(
                "max size must be greater than zero"
            )
        if self.eviction_policy not in ("LRU", "LFU"):
            raise InvalidPolicyError(
                "eviction_policy mist be either 'LRU' or 'LFU'"
            )
        if self.ttl <= 0:
            raise ValueError("ttl must be greater than zero")
        if self.node_count <= 0:
            raise ValueError("node_count must be greater than zero")
