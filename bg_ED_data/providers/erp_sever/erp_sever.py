#!/usr/bin/env python
# -*- coding: utf8 -*-

from bg_ED_data.providers.base.base_provider import BaseProvider

# Suppress ssl warnings
import requests

# requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

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
        cookies = {
            'STDXFWSID': '3prf6nchustns3phuq1om0o881',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.erpsever.bg/bg/prekysvanija',
            'Content-Type': 'application/json; charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            # 'Cookie': 'STDXFWSID=3prf6nchustns3phuq1om0o881',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            'method': 'get_interruptions',
            'region_id': '2',
            'type': 'for_next_48_hours',
            'offset': '0',
            'archive_from_date': '',
            'archive_to_date': '',
        }

        response = requests.get('https://www.erpsever.bg/bg/profil/xhr/', params=params, cookies=cookies, headers=headers)

        response_data_raw = response.text.encode().decode('utf-8-sig')

        print(response_data_raw)


    def get_prices(self, **kwargs):
        url = "https://erpsever.bg/bg/ceni/ceni-za-prenos-i-dostyp"
        response = requests.get(url)
        print(response.text)
        pass
