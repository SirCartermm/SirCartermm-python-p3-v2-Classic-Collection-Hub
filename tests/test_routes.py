#test_routes.py
import pytest
from app import app, db
from models import User, Supercar, Vote, Comment

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client