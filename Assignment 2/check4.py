import requests

url = "http://127.0.0.1:4555/imageapi"
files = {'image': open('{file_path}', 'rb')}
headers = {
    'authorization': "Bearer {token}"
}
response = requests.request("POST", url, files=files)

print(response.text)