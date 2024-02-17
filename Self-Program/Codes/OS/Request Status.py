import urllib3

http = urllib3.PoolManager()
req = http.request('GET', 'http://www.googlee.com')
print(req.status)
