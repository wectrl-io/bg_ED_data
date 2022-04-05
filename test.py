import http.client

conn = http.client.HTTPSConnection("echo.hoppscotch.io")

conn.request("GET", "/")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))