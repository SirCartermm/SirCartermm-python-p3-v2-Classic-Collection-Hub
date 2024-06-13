#test_routes.py
import pytest
from app import app, db
from models import User, Supercar, Vote, Comment

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_registration(client):
    data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password'}
    response = client.post('/register', json=data)
    assert response.status_code == 201

def test_login(client):
    data = {'username': 'testuser', 'password': 'password'}
    response = client.post('/login', json=data)
    assert response.status_code == 200