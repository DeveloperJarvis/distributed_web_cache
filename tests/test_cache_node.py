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
# test_cache_node MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
import time
from core.cache_node import CacheNode


def test_cache_node_initial_state():
    node = CacheNode(key="a", value=b"apple", size=5,)

    assert node.key == "a"
    assert node.value == b"apple"
    assert node.size == 5
    assert node.frequency == 0


def test_cache_node_touch_updates_metadata():
    node = CacheNode(key="a", value=b"apple", size=5,)
    old_access = node.last_accessed
    time.sleep(0.1)

    node.touch()

    assert node.frequency == 1
    assert node.last_accessed > old_access
