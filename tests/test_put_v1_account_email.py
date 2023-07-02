from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "id sit occaecat enim",
        "password": "minim in labore",
        "email": "et laboris ut"
    }
    api.account.put_v1_account_email(
        json=json
    )