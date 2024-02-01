import requests
import json

# URL of the server
login_url = "http://mate-ecfc.onrender.com/login"
data_url = "http://mate-ecfc.onrender.com/data"

# User credentials
credentials = {
    "username": "matedev",
    "password": "4117"
}

# Send a POST request to the login endpoint
response = requests.post(login_url, json=credentials)
if response.status_code == 200:
    token = response.json().get('token')

    # Data you want to add
    data = {
        "key1": "value1",
        "key2": "value2",
        # Add more key-value pairs as needed
    }

    # Send a POST request to the data endpoint
    response = requests.post(data_url, json=data, headers={'Authorization': token})
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
else:
    print(f"Login failed with status code {response.status_code}")
