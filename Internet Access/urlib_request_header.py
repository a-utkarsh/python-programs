import urllib.request

#response = urllib.request.urlopen('https://www.journaldev.com')

#print(response.read())


# Request with Header Data to send User-Agent header
url = 'https://www.journaldev.com'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'

request = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(request)

print(resp.read())

'''We are creating request headers using dictionary and then sending it in the request. 
Above program will print HTML data received from JournalDev home page.'''