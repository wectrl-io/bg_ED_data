#!/usr/bin/env python
# -*- coding: utf8 -*-

# from providers.electrohold.electrohold import Electrohold as Provider
from providers.erp_sever.erp_sever import ERPSever as Provider

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

__class_name__ = ""
"""Provider class name."""

#endregion

def main():

    print("Starting work...")

    provider = Provider()
    ids = ['300066244165', '123456789101']

    for identifier in ids:
        print("Electricity outages data:")
        print(provider.get_outages(identifier=identifier))

    print("Electricity prices data:")
    print(provider.get_prices())

    print("Finitto!")

if __name__ == "__main__":
    main()
