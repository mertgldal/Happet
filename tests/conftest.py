
import pytest
from app import create_app, db
from app.models import User, Animal

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

@pytest.fixture
def create_user(app):
    """Create a user for testing."""
    def _create_user(email, password):
        user = User(username="testuser", name="Test", surname="User", email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    return _create_user
