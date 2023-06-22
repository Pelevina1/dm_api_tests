import requests
import json

url = "http://localhost:5051/v1/account/password"

payload = json.dumps({
  "login": "dolore reprehenderit",
  "token": "urn:uuid:19bec4bd-0857-443b-3d86-67d4cafca843",
  "oldPassword": "qui dolo",
  "newPassword": "nulla eiusmod ad "
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)