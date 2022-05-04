from webbrowser import get
from utils.html_parser import HTMLTableParser
import requests

def _get_data():
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


def get_prices():
    raw_data = _get_data()

    parser = HTMLTableParser()
    parser.feed(raw_data)

    ret_dict = dict()

    for item in parser.tables[0]:
        if len(item) < 2:
            continue

        ret_dict[item[0]] = item[1]

    return ret_dict


def main():
    get_prices()


if __name__ == '__main__':
    main()
