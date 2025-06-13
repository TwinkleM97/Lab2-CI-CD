import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_get(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Contact Form' in response.data

def test_home_page_post_valid_data(client):
    """Test form submission with valid data."""
    response = client.post('/', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Message sent successfully!' in response.data

def test_home_page_post_missing_data(client):
    """Test form submission with missing data."""
    response = client.post('/', data={
        'name': 'Test User',
        'email': '',  # Missing email
        'message': 'This is a test message'
    })
    assert response.status_code == 200
    assert b'Please fill in all fields.' in response.data

def test_flask_app_import():
    """Test that the Flask app can be imported successfully."""
    from app import app
    assert app is not None
    assert app.name == 'app'