#!/usr/bin/env python
# -*- coding: utf8 -*-

from bg_ED_data.providers.electrohold.electrohold import Electrohold
from bg_ED_data.providers.erp_sever.erp_sever import ERPSever

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

__class_name__ = "ERPSever"
"""Provider class name."""

#endregion

class Factory():
    """Providers factory.
    """

    @staticmethod
    def create(provider: str):
        """Providers creator method.

        Args:
            provider (str): The name of wanted provider.

        Raises:
            NotImplementedError: It raise when unknown provider name is passed. 

        Returns:
            any: Instance of the target provider.
        """
        provider_instance = None

        if provider == "erp_sever":
            provider_instance = ERPSever()

        elif provider == "electro_hold":
            provider_instance = Electrohold()

        else:
            raise NotImplementedError("provider not implemented.")

        return provider_instance
