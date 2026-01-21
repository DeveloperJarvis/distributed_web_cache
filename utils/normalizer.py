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
# normalizer MODULE
# --------------------------------------------------
"""
Normalization utilities for cache keys and HTTP resources.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from exceptions.errors import InvalidKeyError


def normalize_key(key: str) -> str:
    """
    Normalize cache keys for consistent hashing and lookup.
    - Strips whitespace
    - Converts to lowercase
    """
    if key is None:
        return ""
    
    if not isinstance(key, str):
        raise InvalidKeyError("Cache must be a string")
    
    return key.strip().lower()


def normalize_url(url: str) -> str:
    """
    Normalize HTTP URLs before caching.
    """
    if url is None:
        return ""
    
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    
    return url.strip()
