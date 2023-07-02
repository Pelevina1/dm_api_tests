from services.dm_api_account import DmApiAccount


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "test234",
        "password": "test234",
        "rememberMe": True
    }
    api.login.post_v1_account_login(
        json=json
    )
