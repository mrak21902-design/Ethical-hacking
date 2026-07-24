import requests

response = requests.get("https://api.github.com")

data = response.json()

print("Current User URL:", data["current_user_url"])
print("User URL:", data["user_url"])
print("Repository URL:", data["repository_url"])
