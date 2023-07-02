from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "dolore reprehenderit",
        "token": "urn:uuid:19bec4bd-0857-443b-3d86-67d4cafca843",
        "oldPassword": "qui dolo",
        "newPassword": "nulla eiusmod ad "
    }
    api.account.put_v1_account_password(
        json=json
    )
