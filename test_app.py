import pytest
from app import app  # Import the Flask app

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.testing = True  # Enable testing mode
    client = app.test_client()
    return client

def test_home_page(client):
    """Test if the home route ('/') returns status code 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Flask App" in response.data  # Check content

def test_invalid_page(client):
    """Test a non-existing route."""
    response = client.get('/invalid')
    assert response.status_code == 404
