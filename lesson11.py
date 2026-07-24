import urllib.request
import json

url = "https://api.github.com"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print(data)
