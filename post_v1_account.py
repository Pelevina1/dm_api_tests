import requests
import json

url = "http://localhost:5051/v1/account"

payload = json.dumps({
  "login": "test234",
  "email": "test234@mail.ru",
  "password": "test234"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)




