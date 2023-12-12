import requests
import json

url = ("https://stage-can-services.cbs.com/canServices/video/search.json?token=2a5a34ac4599f81e55070c4f242a914b&count"
       "=10&o=title,contentId,regionalRatings&country=BR")
url1 = 'https://stage-can-services.cbs.com/canServices/video/search.json'

payload = {}
headers = {}
params = {
    'token': '2a5a34ac4599f81e55070c4f242a914b',
    'count': 10,
    'o': 'title,contentId,regionalRatings',
    'country': 'BR'
     }

response = requests.request("GET", url)
# response = requests.request("GET", url, headers=headers, data=payload)

print(json.dumps(response.json(), indent=3))

response1 = requests.request('GET', url1, params=params)

print(json.dumps(response1.json(), indent=3))

