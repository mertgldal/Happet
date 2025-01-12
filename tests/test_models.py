from app.models import User, Animal
from app import db

def test_user_model(create_user):
    """Test the User model."""
    user = create_user("test@example.com", "password123")
    assert user.email == "test@example.com"
    assert user.username == "testuser"

def test_animal_model(app):
    """Test the Animal model."""
    with app.app_context():
        animal = Animal(
            user_id=1,
            animal_name="Buddy",
            animal_type="Dog",
            animal_gender="Male",
            animal_age=24,
            animal_color="Brown",
            history="Friendly dog",
            character="Playful",
            behavioral_features="Good with kids",
            preferences="Loves outdoors",
            image_url="http://example.com/image.jpg",
        )
        db.session.add(animal)
        db.session.commit()

        saved_animal = Animal.query.first()
        assert saved_animal.animal_name == "Buddy"
        assert saved_animal.animal_age == 24
