from services.dm_api_account import DmApiAccount


def test_delete_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    api.login.delete_v1_account_login()