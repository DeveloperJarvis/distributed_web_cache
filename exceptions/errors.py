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
# erros MODULE
# --------------------------------------------------
"""
Custom exception hierarchy for Distributed Web Cache.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# distributed cache error
# --------------------------------------------------
class DistributedCacheError(Exception):
    """
    Base exception for all distributed cache errors.
    """
    pass


# --------------------------------------------------
# validation errors
# --------------------------------------------------
class InvalidKeyError(DistributedCacheError):
    """
    Raised when a cache key is invalid.
    """
    pass


class InvalidPolicyError(DistributedCacheError):
    """
    Raised when an unsupported eviction policy is provided.
    """
    pass


class InvalidSizeError(DistributedCacheError):
    """
    Raised when cache size configuration is invalid.
    """
    pass


# --------------------------------------------------
# storage errors
# --------------------------------------------------
class StorageError(DistributedCacheError):
    """
    Raised for storage-related failures.
    """
    pass


# --------------------------------------------------
# cache operation errors
# --------------------------------------------------
class CacheMissError(DistributedCacheError):
    """
    Raised when a requested key is not found in cache.
    """
    pass


class CacheNodeError(DistributedCacheError):
    """
    Raised for cache node-specific failures.
    """
    pass


class EvictionError(DistributedCacheError):
    """
    Raised when eviction fails or is misconfigured.
    """
    pass
