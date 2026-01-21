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
# test_utils MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from utils.normalizer import normalize_key, normalize_url
from utils.validators import (
    validate_key,
    validate_cache_size,
    validate_eviction_policy,
)
from exceptions.errors import (
    InvalidKeyError,
    InvalidSizeError,
    InvalidPolicyError,
)


def test_normalize_key():
    assert normalize_key("  ABC ") == "abc"


def test_normalize_key_none():
    assert normalize_key(None) == ""


def test_validate_key_failure():
    with pytest.raises(InvalidKeyError):
        validate_key("")


def test_validate_cache_size():
    validate_cache_size(10)
    with pytest.raises(InvalidSizeError):
        validate_cache_size(0)


def test_validate_eviction_policy():
    validate_eviction_policy("LRU")
    with pytest.raises(InvalidPolicyError):
        validate_eviction_policy("FIFO")
