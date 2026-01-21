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
# defaults MODULE
# --------------------------------------------------
"""
Default configuration values for Distributed Web Cache
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# Default max entries per cache node
DEFAULT_MAX_SIZE: int = 100

# Default evivtion policy: "LRU" or "LFU"
DEFAULT_EVICTION_POLICY: str = "LRU"

# Default TTL (time-to-live) for cached entries (seconds)
DEFAULT_TTL: int = 3600

# Default number of nodes in distributed cache
DEFAULT_NODE_COUNT: int = 3
