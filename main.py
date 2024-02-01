import requests

# Define the URL of your server API endpoint
url = 'https://mate-ecfc.onrender.com/data'

# Define the data you want to add
data_to_add = {
    'key': 'example_key',
    'value': 'example_value'
}

# Send a POST request to add the data
response = requests.post(url, json=data_to_add)

# Check the response
if response.status_code == 200:
    print('Data added successfully.')
else:
    print('Failed to add data.')
