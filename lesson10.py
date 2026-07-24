import urllib.request

url = "https://example.com"

response = urllib.request.urlopen(url)

print("Status:", response.status)
print("\nHeaders:\n")
print(response.headers)
