#!/usr/bin/env python
# -*- coding: utf8 -*-

from enum import Enum

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

__class_name__ = "Province"
"""Provider class name."""

#endregion

class Province(Enum):
    """Province enum class for ERPSever geo regions.
    """

    NONE = 0
    VARNA = 1
    VELIKO_TARNOVO = 2
    GABROVO = 3
    DOBRICH = 4
    RAZGRAD = 5
    RUSE = 6
    SILISTRA = 7
    TARGOVISHTE = 8
    SHUMEN = 9
