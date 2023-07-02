from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "ad labore ut magna irure",
        "email": "proident aliquip"
    }
    api.account.post_v1_account_password(
        json=json
    )
