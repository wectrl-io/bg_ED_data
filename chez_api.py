import http.client, urllib.parse

conn = http.client.HTTPSConnection("info.cez.bg")

params = urllib.parse.urlencode({
    # '@Content-Disposition': 'form-data', 
    '@action': 'viewitn',
    '@itn': '310228147475',
    '@lat': 0,
    '@lon': 0})

# payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\nviewitn\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"itn\"\r\n\r\n310228147475\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"lat\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"lon\"\r\n\r\n0\r\n-----011000010111000001101001--\r\n\r\n"

headers = {
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "keep-alive",
    'Content-Length': "29",
    'Content-Type': "multipart/form-data; boundary=---011000010111000001101001",
    # 'Cookie': "cookie_consent_user_accepted=true; itn_list=300066244165; PHPSESSID=53fkpqnhr3hplpe3gcsc05nu26; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D",
    'Host': "info.cez.bg",
    'Origin': "https://info.cez.bg",
    'Referer': "https://info.cez.bg/webint/vok/avplan.php?BBKING=FYI",
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest"
}

conn.request("POST", "/webint/vok/avplan.php", params, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))