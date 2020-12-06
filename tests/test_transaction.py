from fastapi import FastAPI

from fastapi.testclient import TestClient
from main import app
from sql_app.account_repository import AccountRepository

client = TestClient(app)


def test_read_main():

    response = client.post("/transaction", json={
        "amount": 100,
        "dest_account_email": "contact@maxime-moreau.fr"
    })

    # I'm not authenticated -> 404
    assert response.status_code == 401

    user_res = client.post('/users/', json={
        'email': 'contact@maxime-moreau.fr',
        'password': 'coucou'
    })

    users_res = client.get('/users')
    users = users_res.json()

    assert users[0] == {'email': 'contact@maxime-moreau.fr', 'id': 1}

    user_token_res = client.post(
        "token",
        data={
            'username': 'contact@maxime-moreau.fr',
            'password': 'coucou'
        }
    )

    assert user_token_res.status_code == 200

    user_token = user_token_res.json()['access_token']

    print(user_token_res.json())

    transaction_res = client.post(
        "/transaction",
        headers={"Authorization": f"Bearer {user_token}"},
        json={
            "amount": 100,
            "dest_account_email": "contact2@maxime-moreau.fr"
        }
    )

    # Not enough money!
    assert transaction_res.status_code == 400

    account_repository = AccountRepository()


    # assert response.status_code == 200
