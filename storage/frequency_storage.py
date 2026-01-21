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
# frequency_storage MODULE
# --------------------------------------------------
"""
Frequency storage for cache access patterns.
Used primarily by LFU eviction policy
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from threading import Lock
from typing import Dict
from exceptions.errors import StorageError


# --------------------------------------------------
# frequency storage
# --------------------------------------------------
class FrequencyStorage:
    """
    Thread-safe in-memory frequency counter.
    """

    def __init__(self) -> None:
        self._frequencies: Dict[str, int] = {}
        self._lock = Lock()
    
    def increment(self, key: str) -> int:
        """
        Increment access frequency for a key.
        """
        if not key:
            raise StorageError("Key cannot be empty")
        
        with self._lock:
            self._frequencies[key] = (
                self._frequencies.get(key, 0) + 1)
            return self._frequencies[key]
    
    def get(self, key: str) -> int:
        """
        Get frequency count for a key.
        """
        with self._lock:
            return self._frequencies.get(key, 0)
    
    def remove(self, key: str) -> None:
        """
        Remove a key from frequency tracking.
        """
        with self._lock:
            self._frequencies.pop(key, None)
        
    def clear(self) -> None:
        """
        Clear all frequency data.
        """
        with self._lock:
            self._frequencies.clear()
