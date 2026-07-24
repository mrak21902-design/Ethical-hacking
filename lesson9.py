import urllib.request

url = input("Website URL likho(https://...): ")

response = urllib.request.urlopen(url)

print("Status code:" ,response.status)

html = response.read().decode("utf-8")

print(html[:500])

