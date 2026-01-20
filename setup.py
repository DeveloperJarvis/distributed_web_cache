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
# setup MODULE
# --------------------------------------------------
"""
Distributed Web Cache
Setup script
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from setuptools import setup, find_packages
from pathlib import Path


ROOT = Path(__file__).parent


setup(
    name="distributed-web-cache",
    version="0.1.0",
    description="HTTP caching layer with distributed nodes and eviction policies (LRU/LFU)",
    long_description=(ROOT / "README.md").read_text(
        encoding="utf-8"
    ),
    long_description_content_type="text/markdown",
    author="Developer Jarvis",
    author_email="developerjarvis@github.com",
    url="https://github.com/DeveloperJarvis/distributed_web_cache",
    license="GPL-3.0-or-later",
    packages=find_packages(
        exclude=["tests*", "examples*", "logs*"]
    ),
    python_requires=">=3.9",
    install_requires=[
        "typing-extensions>=4.0.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ]
    },
    entry_points={
        "console_scripts": [
            "distributed-cache=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Appproved :: GNU General Public License v3 or later",
        "Operating System :: OS Independent",
        "Topic :: Software Developement :: Libraries",
        "Topic :: System :: Networking :: Caching",
    ],
    include_package_data=True,
    zip_safe=False,
)
