import requests


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://localhost:5051/v1/account/email"

    payload = {
        "login": "id sit occaecat enim",
        "password": "minim in labore",
        "email": "et laboris ut"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )
    return response
