#!/usr/bin/env python
# -*- coding: utf8 -*-

import json

from providers.base.base_provider import BaseProvider
from utils.html_parser import HTMLTableParser

# Suppress ssl warnings
import requests
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

from webbrowser import get

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

__class_name__ = "Electrohold"
"""Provider class name."""

#endregion

class Electrohold(BaseProvider):

#region Attributes

    __actions = {}

#endregion

#region Constructor

    def __init__(self, **kwargs):
        super().__init__()

        self.__actions = {
            'verify': 'chkca',
            'check_current': 'viewitn',
            'check_planned': 'viewitn_plan'
        }

#endregion

#region Private Methods

    def __get_outages_data(self, client_id, check_type):

        if isinstance(client_id, int):
            client_id = str(client_id)

        data = {
            'action': self.__actions[check_type],
            'itn': client_id
        }

        response = requests.post('https://info.electrohold.bg/webint/vok/avplan.php', data=data, verify=False)
        response_data_raw = response.text.encode().decode('utf-8-sig')

        return response_data_raw

    def __get_data(self):

        cookies = {
            'CookieConsent': '{stamp:%27TeYLewhoCDnnTI5k1JA3sFfal8xPsnYzIFb7iW84iBfc64uVW4E40Q==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1651568457174%2Cregion:%27bg%27}',
        }

        headers = {
            'authority': 'ermzapad.bg',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9,bg;q=0.8',
            # 'cookie': 'CookieConsent={stamp:%27TeYLewhoCDnnTI5k1JA3sFfal8xPsnYzIFb7iW84iBfc64uVW4E40Q==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1651568457174%2Cregion:%27bg%27}',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }

        response = requests.get('https://ermzapad.bg/bg/za-klienta/ceni-i-nachini-na-plashane/ceni-za-dostp-i-prenos/', cookies=cookies, headers=headers)

        return response.text

#endregion

#region Public Methods

    def get_outages(self, cid):

        actions = self.__actions.keys()

        ret_data = dict()

        for action in actions:
            raw_data = self.__get_outages_data(cid, action)

            if "няма планирани прекъсвания" in raw_data or "няма регистрирано планирано" in raw_data:
                ret_data[action] = None
            else:
                ret_data[action] = json.loads(raw_data)

        return ret_data

    def get_prices(self):

        raw_data = self.__get_data()

        parser = HTMLTableParser()
        parser.feed(raw_data)

        ret_dict = dict()

        for item in parser.tables[0]:
            if len(item) < 2:
                continue

            ret_dict[item[0]] = item[1]

        return ret_dict

#endregion
