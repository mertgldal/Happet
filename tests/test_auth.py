import pytest
from app import create_app, db
from app.models import User
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    """Fixture to set up a test client."""
    app = create_app(config_name='testing')  # Use the testing config
    with app.test_client() as client:
        # Set up the application context for the test
        with app.app_context():
            db.create_all()  # Create the test database
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the test



def test_register_user_invalid_form(client):
    """Test invalid registration due to form validation errors."""
    # Attempt to submit a form with mismatched passwords
    response = client.post('/register', data={
        'username': 'testuser',
        'name': 'Test',
        'surname': 'User',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'wrongpassword',  # Mismatch with password
    })

    # Check for successful form submission (status code 200 for form re-render)
    assert response.status_code == 200

    # Ensure the validation error message for password mismatch is present
    assert b'Passwords must match' in response.data

def test_register_user_missing_fields(client):
    """Test registration with missing required fields."""
    # Attempt to submit a form with missing fields (e.g., missing username)
    response = client.post('/register', data={
        'name': 'Test',
        'surname': 'User',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123',
    })

    # Check for successful form submission (status code 200 for form re-render)
    assert response.status_code == 200

    # Ensure a validation error message for missing username
    assert b'This field is required.' in response.data
