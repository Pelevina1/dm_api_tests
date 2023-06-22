import requests

url = "http://localhost:5051/v1/account/cb4e9c8e-0960-4c72-b457-fdc4aea293d6"

payload={}
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
