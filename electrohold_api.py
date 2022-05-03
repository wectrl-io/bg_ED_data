from http import client
import requests
import json

client_id = '300066244165'

actions = {
    'verify': 'chkca',
    'check_current': 'viewitn',
    'check_planned': 'viewitn_plan'
}

cookies = {
    'PHPSESSID': 'qinr49ekethesbsoschpusre56',
    'cookie_consent_user_accepted': 'true',
    'itn_list': '',
    'cookie_consent_level': '%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=qinr49ekethesbsoschpusre56; cookie_consent_user_accepted=true; itn_list=; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
    'Origin': 'https://info.electrohold.bg',
    'Referer': 'https://info.electrohold.bg/webint/vok/avplan.php?BBKING=FYI',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'action': actions['check_planned'],
    'itn': client_id,
    'lat': 0,
    'lon': 0
}

response = requests.post('https://info.electrohold.bg/webint/vok/avplan.php', cookies=cookies, headers=headers, data=data, verify=False)
response_data_raw = response.text.encode().decode('utf-8-sig')
# response_dict = json.loads(response_data_raw)

print(response_data_raw)