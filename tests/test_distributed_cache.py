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
# test_distributed_cache MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from core.distributed_cache import DistributedCache
from config.engine_config import CacheConfig
from exceptions.errors import CacheMissError, InvalidPolicyError


def test_put_and_get_across_nodes():
    config = CacheConfig(node_count=2, max_size=100)
    cache = DistributedCache(config)

    cache.put("key1", b"value1")
    cache.put("key2", b"value2")

    assert cache.get("key1") == b"value1"
    assert cache.get("key2") == b"value2"


def test_cache_miss_raises_error():
    config = CacheConfig(node_count=2, max_size=100)
    cache = DistributedCache(config)

    with pytest.raises(CacheMissError):
        cache.get("missing")
    

def test_invalid_eviction_policy():
    with pytest.raises(InvalidPolicyError):
        DistributedCache(
            CacheConfig(eviction_policy="INVALID")
        )
