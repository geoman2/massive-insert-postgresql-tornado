import json
import pytest
import requests

BASE_URL = 'http://localhost:8080'

DATA = {
    "messages": [
        {"message": "hello world"},
        {"message": "bonjour tout le monde"},
        {"message": "da jia hao"}
    ]
}

def test_post_insert_transaction():
    r = requests.post(
        BASE_URL + '/insert-transaction',
        headers={'Content-type': 'application/json'},
        data=json.dumps(DATA)
    )
    assert r.status_code == 200

def test_post_multiple_inserts():
    r = requests.post(
        BASE_URL + '/multiple-inserts',
        headers={'Content-type': 'application/json'},
        data=json.dumps(DATA)
    )

    assert r.status_code == 200

def test_post_copy_handler():
    r = requests.post(BASE_URL + '/copy')
    assert r.status_code == 200
