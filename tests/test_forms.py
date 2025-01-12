import pytest
from app import create_app
from app.forms import RegisterForm


@pytest.fixture
def app():
    """Create and return a Flask app instance for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,  # Disable CSRF for testing
    })
    yield app


@pytest.fixture
def client(app):
    """Provide a test client for the Flask application."""
    return app.test_client()


def test_register_form_valid(app):
    """Test valid data for the RegisterForm."""
    with app.app_context():  # Ensure app context is pushed for the form
        form = RegisterForm(data={
            "username": "testuser",
            "name": "Test",
            "surname": "User",
            "email": "test@example.com",
            "password": "password123",
            "confirm_password": "password123",
        })

        # Now you can assert form validity
        assert form.validate()  # Should pass validation
