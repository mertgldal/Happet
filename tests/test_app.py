from app import db # Import db and app from your Flask application module

def test_app_factory(app):
    """Test that the app factory creates an app instance."""
    assert app is not None
    assert app.testing

def test_database_initialization(app):
    """Test that the database initializes correctly."""
    with app.app_context():
        from app.models import User, Animal
        assert db.session.query(User).count() == 0
        assert db.session.query(Animal).count() == 0
