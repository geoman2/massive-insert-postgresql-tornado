import pytest
import requests

BASE_URL = 'http://localhost:8080'

def test_post_insert_transaction():
    r = requests.post(BASE_URL + '/insert-transaction')
    assert r.status_code == 200

def test_post_multiple_inserts():
    r = requests.post(BASE_URL + '/multiple-inserts')
    assert r.status_code == 200

def test_post_copy_handler():
    r = requests.post(BASE_URL + '/copy')
    assert r.status_code == 200
