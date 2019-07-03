import requests
import json

email = 'utkarsh123bholu@gmail.com'
params = {'email': email}

response = requests.get('http://emailpie.com/v1/check', params=params)
#print(response.json())
response = json.loads(response)

print(response)