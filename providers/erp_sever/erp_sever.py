#!/usr/bin/env python
# -*- coding: utf8 -*-

from providers.base.base_provider import BaseProvider

# Suppress ssl warnings
import requests
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

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

class ERPSever(BaseProvider):

    def get_outages(self, **kwargs):
        url = "https://erpsever.bg/bg/profil/xhr/?method=get_interruptions&region_id=2&type=for_next_48_hours&offset=0&archive_from_date=&archive_to_date="
        response = requests.get(url)
        response_data_raw = response.text.encode().decode('utf-8-sig')
        print(response_data_raw)


    def get_prices(self, **kwargs):
        url = "https://erpsever.bg/bg/ceni/ceni-za-prenos-i-dostyp"
        response = requests.get(url)
        pass
