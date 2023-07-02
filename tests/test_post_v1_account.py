from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "test23425",
        "email": "test234457@mail.ru",
        "password": "test234334"
    }
    api.account.post_v1_account(
        json=json
    )
    token = "1232345"
    api.account.put_v1_account_token(
        token=token
    )
