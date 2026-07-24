import requests

username = input("GitHub Username: ")

try:
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()

    print("Name:", data["name"])
    print("Followers:", data["followers"])
    print("Public Repos:", data["public_repos"])

except Exception as e:
    print("Error:", e)
