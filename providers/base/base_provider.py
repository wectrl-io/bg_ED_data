#!/usr/bin/env python
# -*- coding: utf8 -*-

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

__class_name__ = "BaseProvider"
"""Provider class name."""

#endregion

class BaseProvider:

    def __init__(self):
        pass

    def get_outages(self, **kwargs):
        pass

    def get_prices(self, **kwargs):
        pass
