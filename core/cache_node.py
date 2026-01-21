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
# cache_node MODULE
# --------------------------------------------------
"""
Cache node abstraction.
Represents a single cache entry.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import time
from dataclasses import dataclass, field


# --------------------------------------------------
# cache node
# --------------------------------------------------
@dataclass
class CacheNode:
    """
    Represents a single cached object.
    """
    key: str
    value: bytes
    size: int

    frequency: int = 0
    last_accessed: float = field(default_factory=time.time)
    created_at: float = field(default_factory=time.time)

    def touch(self) -> None:
        """
        Update access metadata.
        """
        self.frequency += 1
        self.last_accessed = time.time()
