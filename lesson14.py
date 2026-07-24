import requests

username = input("GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

data = response.json()

print("Name:", data.get("name"))
print("Followers:", data.get("followers"))
print("Public Repos:", data.get("public_repos"))
