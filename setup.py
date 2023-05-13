#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import find_packages, setup

#region File Attributes

__author__ = "Orlin Dimitrov"
"""Author of the file."""

__copyright__ = ""
"""Copyrighted"""

__credits__ = []
"""Credits"""

__license__ = ""
"""License
@see """

__version__ = "1.0.0"
"""Version of the file."""

__maintainer__ = ["Orlin Dimitrov", "Martin Maslyankov", "Nikola Atanasov"]
"""Name of the maintainer."""

__email__ = ""
"""E-mail of the author."""

#endregion

setup(
    name="bg_ED_data",
    packages=find_packages(include=["bg_ED_data"]),
    version=__version__,
    description="Bulgaria electro distribution data provider.",
    author=__author__,
    license=__license__,
    install_requires=[],
    setup_requires=[],
    tests_require=["certifi==2022.12.7", "charset-normalizer==3.1.0",
                   "idna==3.4", "requests==2.28.2", "urllib3==1.26.15"],
    test_suite="",
)
