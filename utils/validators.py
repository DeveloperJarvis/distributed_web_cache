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
# validators MODULE
# --------------------------------------------------
"""
Validation helpers for Distributed Web Cache.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from exceptions.errors import (
    InvalidKeyError,
    InvalidPolicyError,
    InvalidSizeError,
)


def validate_key(key: str) -> None:
    """
    Validate cache key.
    """
    if not isinstance(key, str):
        raise InvalidKeyError("Cache key must be a string")
    if not key.strip():
        raise InvalidKeyError("Cache key cannot be empty")


def validate_eviction_policy(policy: str) -> None:
    """
    Validate eviction policy.
    """
    if policy not in ("LRU", "LFU"):
        raise InvalidPolicyError(
            "Eviction policy must be 'LRU' or 'LFU'"
        )


def validate_cache_size(size: int) -> None:
    """
    Validate cache size.
    """
    if not isinstance(size, int):
        raise InvalidSizeError(
            "Cache size must be an integer"
        )
    if size <= 0:
        raise InvalidSizeError(
            "Cache size must be greater than zero"
        )
