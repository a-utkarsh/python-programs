import urllib.request
import urllib.parse

post_url = 'http://localhost:3000/employees'

headers = {}
headers['Content-Type'] = 'application/json'

# POST request encoded data
post_data = urllib.parse.urlencode({'name' : 'Anand', 'salary'  : '199880'}).encode('ascii')

#Automatically calls POST method because request has data
post_response = urllib.request.urlopen(url=post_url, data=post_data)

print(post_response.read())