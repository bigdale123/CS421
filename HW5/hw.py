import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

# Send a GET request to retrieve the challenge
response = requests.get(url)

# Extract the challenges from the response
challenges = response.json()
print(challenges)

for challenge in challenges:
    print("Result for challenge "+str(challenge["id"])+": "+str(eval(challenge["problem"][:-1])))