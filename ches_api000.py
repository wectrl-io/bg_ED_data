import requests


# https://info.cez.bg/webint/vok/avplan.php

def parse_page(): 
    cookies = {
        'PHPSESSID': 'mkhk8n8f25sam96odv40s544a3',
        'cookie_consent_user_accepted': 'true',
        'itn_list': '',
        'cookie_consent_level': '%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://info.cez.bg',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://info.cez.bg/webint/vok/avplan.php?BBKING=FYI',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'PHPSESSID=mkhk8n8f25sam96odv40s544a3; cookie_consent_user_accepted=true; itn_list=; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
    }

    data = {
        'action': 'chkca',
        'itn': '300066244165',
    }

    response = requests.post('https://info.cez.bg/webint/vok/avplan.php', headers=headers, cookies=cookies, data=data)

    return response

def main():
    print("Hello!")

    test_run = parse_page()

    print(test_run)

if __name__=='__main__':
    main()