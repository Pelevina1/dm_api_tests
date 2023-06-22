import requests
import json

url = "http://localhost:5051/v1/account/email"

payload = json.dumps({
  "login": "id sit occaecat enim",
  "password": "minim in labore",
  "email": "et laboris ut"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)