import requests

def call_api(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
url = 'http://localhost:5000/api/post'  # Replace with the actual URL of your API

data = {
    'image': r'path'  # Replace with the path to your image file
}
result = call_api(url, data)
if result:
    print(result['message'])
else:
    print("API call failed")