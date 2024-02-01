import requests

# Define the URL of the server's API endpoint
url = 'https://mate-ecfc.onrender.com/data'

# Sample data to add
data_to_add = {
    'new_key': 'new_value'
}

# Define the username and password for authentication
username = 'matedev'
password = '4117'

try:
    # Send a POST request with authentication credentials
    response = requests.post(url, json=data_to_add, auth=(username, password))

    # Check the response status code
    if response.status_code == 200:
        print('Data added successfully.')
    else:
        print(f'Failed to add data. Status code: {response.status_code}')
except Exception as e:
    print(f'Error: {e}')
