import urllib.request

response = urllib.request.urlopen('http://www.google.com')

print(response.info())

print('Response Content Type is = ', response.info()["content-type"])

