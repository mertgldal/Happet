# from app import db, app  # Import db and app from your Flask application module
from app import db # Import db and app from your Flask application module
from app import create_app
from app.models import Animal, User  # Import the Animal and User models
from werkzeug.security import generate_password_hash  # Import password hashing function

app = create_app()

animals = [
    {
        "user_id": 1,
        "animal_name": "Ben",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 4,
        "animal_color": "Beige",
        "history": "Ben was left in a shelter before the war broke out.",
        "character": "Ben is very fond of company, gets along well with people and other dogs.",
        "behavioral_features": "Calm, quick to learn and memorize commands, accustomed to walking.",
        "preferences": "Not on a chain. Ben thrives with a loving person.",
        "image_url": "https://images.unsplash.com/photo-1534361960057-19889db9621e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZG9nfGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 2,
        "animal_name": "Leila",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 2,
        "animal_color": "Grey",
        "history": "Leila was found as a stray kitten near an abandoned warehouse.",
        "character": "Playful and curious, loves exploring new places.",
        "behavioral_features": "Independent yet affectionate, enjoys quiet naps in sunny spots.",
        "preferences": "Prefers a calm household with minimal disruptions.",
        "image_url": "https://images.unsplash.com/photo-1472491235688-bdc81a63246e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 3,
        "animal_name": "Peachy",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 16,
        "animal_color": "White",
        "history": "Peachy was rescued from a puppy mill and rehabilitated by volunteers.",
        "character": "Friendly and outgoing, adores meeting new people.",
        "behavioral_features": "House-trained, quick learner, and enjoys outdoor play.",
        "preferences": "Ideal for an active family that loves long walks.",
        "image_url": "https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRvZ3xlbnwwfDB8MHx8fDI%3D"
    },
    {
        "user_id": 4,
        "animal_name": "Bead",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 23,
        "animal_color": "Beige",
        "history": "Bead spent most of her life in a loving home but was surrendered due to allergies.",
        "character": "Gentle and laid-back, enjoys quiet companionship.",
        "behavioral_features": "Easily adapts to new environments, loves being brushed.",
        "preferences": "Needs a cozy indoor home with soft spots to rest.",
        "image_url": "https://images.unsplash.com/photo-1511044568932-338cba0ad803?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 5,
        "animal_name": "Mars",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 37,
        "animal_color": "White",
        "history": "Mars was found wandering in a rural area and was brought to a shelter.",
        "character": "Energetic and playful, loves fetching balls.",
        "behavioral_features": "Highly trainable, enjoys agility exercises.",
        "preferences": "Requires a spacious yard and an active owner.",
        "image_url": "https://images.unsplash.com/photo-1455287278107-115faab3eafa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGRvZ3xlbnwwfDB8MHx8fDI%3D"
    },
    {
        "user_id": 6,
        "animal_name": "Zhuzha",
        "animal_type": "Dog",
        "animal_gender": "Female",
        "animal_age": 28,
        "animal_color": "Brown",
        "history": "Zhuzha was a farm dog before being rehomed to a city.",
        "character": "Protective and loyal, forms strong bonds with family.",
        "behavioral_features": "Obedient and calm, responds well to commands.",
        "preferences": "Prefers a quiet home with plenty of outdoor time.",
        "image_url": "https://images.unsplash.com/photo-1507146426996-ef05306b995a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8ZG9nfGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 1,
        "animal_name": "Bagel",
        "animal_type": "Cat",
        "animal_gender": "Male",
        "animal_age": 45,
        "animal_color": "Brown",
        "history": "Bagel was rescued from a hoarding situation.",
        "character": "Shy at first but very affectionate once comfortable.",
        "behavioral_features": "Loves climbing and exploring high spaces.",
        "preferences": "Needs a patient owner and a tall cat tree.",
        "image_url": "https://images.unsplash.com/photo-1489084917528-a57e68a79a1e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 2,
        "animal_name": "Lord",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 48,
        "animal_color": "Beige",
        "history": "Lord was abandoned in a park and rescued by volunteers.",
        "character": "Regal and composed, enjoys quiet walks and attention.",
        "behavioral_features": "Well-mannered and calm, good with children.",
        "preferences": "Would thrive in a family home with a garden.",
        "image_url": "https://images.unsplash.com/photo-1534361960057-19889db9621e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZG9nfGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 3,
        "animal_name": "Sonata",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 3,
        "animal_color": "Grey",
        "history": "Sonata was born in a foster home and raised with care.",
        "character": "Playful and curious, adores string toys.",
        "behavioral_features": "Very social, loves being around people and other cats.",
        "preferences": "Great for a multi-pet household.",
        "image_url": "https://images.unsplash.com/photo-1501820488136-72669149e0d4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 3,
        "animal_name": "Milo",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 12,
        "animal_color": "Black",
        "history": "Milo was saved from a busy highway as a puppy.",
        "character": "Adventurous and brave, loves exploring new places.",
        "behavioral_features": "Highly intelligent and learns quickly.",
        "preferences": "Best suited for an owner who enjoys outdoor activities.",
        "image_url": "https://images.unsplash.com/photo-1422565096762-bdb997a56a84?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9nfGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 1,
        "animal_name": "Luna",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 5,
        "animal_color": "White",
        "history": "Luna was found as a stray near a shopping center.",
        "character": "Gentle and loving, enjoys being held.",
        "behavioral_features": "Very clean, prefers a tidy environment.",
        "preferences": "Would love a quiet home with plenty of attention.",
        "image_url": "https://images.unsplash.com/photo-1478098711619-5ab0b478d6e6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 4,
        "animal_name": "Max",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 30,
        "animal_color": "Brown",
        "history": "Max grew up in a family but was rehomed due to moving.",
        "character": "Friendly and loyal, enjoys being around children.",
        "behavioral_features": "Very calm and obedient, loves car rides.",
        "preferences": "Thrives in a family environment.",
        "image_url": "https://images.unsplash.com/photo-1455287278107-115faab3eafa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGRvZ3xlbnwwfDB8MHx8fDI%3D"
    },
    {
        "user_id": 4,
        "animal_name": "Bella",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 18,
        "animal_color": "Grey",
        "history": "Bella was surrendered due to her owner's illness.",
        "character": "Affectionate and cuddly, enjoys being near people.",
        "behavioral_features": "Quiet and relaxed, loves being brushed.",
        "preferences": "Needs a serene home where she can feel safe.",
        "image_url": "https://images.unsplash.com/photo-1472491235688-bdc81a63246e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 5,
        "animal_name": "Rex",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 50,
        "animal_color": "Black and White",
        "history": "Rex was a working dog on a ranch before retiring.",
        "character": "Highly intelligent and protective, loves structured tasks.",
        "behavioral_features": "Knows many commands, thrives on routine.",
        "preferences": "Best with an experienced dog owner.",
        "image_url": "https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGRvZ3xlbnwwfDB8MHx8fDI%3D"
    },
    {
        "user_id": 5,
        "animal_name": "Mochi",
        "animal_type": "Cat",
        "animal_gender": "Female",
        "animal_age": 9,
        "animal_color": "Cream",
        "history": "Mochi was adopted as a kitten but returned due to allergies.",
        "character": "Sweet and playful, loves interactive toys.",
        "behavioral_features": "Very adaptable and easygoing.",
        "preferences": "Would love a home with windows to watch birds.",
        "image_url": "https://images.unsplash.com/photo-1501820488136-72669149e0d4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 6,
        "animal_name": "Shadow",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 22,
        "animal_color": "Black",
        "history": "Shadow was found tied to a pole in an abandoned lot.",
        "character": "Cautious but warms up to people with patience.",
        "behavioral_features": "Loves running and playing fetch.",
        "preferences": "Best for an active owner who can help build confidence.",
        "image_url": "https://images.unsplash.com/photo-1507146426996-ef05306b995a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8ZG9nfGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 6,
        "animal_name": "Pumpkin",
        "animal_type": "Cat",
        "animal_gender": "Male",
        "animal_age": 15,
        "animal_color": "Orange",
        "history": "Pumpkin was rescued from a storm drain as a kitten.",
        "character": "Playful and mischievous, loves chasing toys.",
        "behavioral_features": "Very social and loves human interaction.",
        "preferences": "Great for a home with children.",
        "image_url": "https://images.unsplash.com/photo-1478098711619-5ab0b478d6e6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y2F0fGVufDB8MHwwfHx8Mg%3D%3D"
    },
    {
        "user_id": 1,
        "animal_name": "Buddy",
        "animal_type": "Dog",
        "animal_gender": "Male",
        "animal_age": 24,
        "animal_color": "Golden",
        "history": "Buddy was surrendered after his owner moved overseas.",
        "character": "Loyal and protective, great with kids.",
        "behavioral_features": "Loves learning new tricks and games.",
        "preferences": "Best with a family that enjoys outdoor activities.",
        "image_url": "https://images.unsplash.com/photo-1455287278107-115faab3eafa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGRvZ3xlbnwwfDB8MHx8fDI%3D"
    }
]



# Dummy data for users with updated names
users = [
    {"username": "mertgl", "name": "Mert", "surname": "Guldal", "email": "mert@example.com", "password": "password123"},
    {"username": "alexyr", "name": "Alex", "surname": "Yurchak", "email": "alex@example.com", "password": "password123"},
    {"username": "yostinash", "name": "Yostina", "surname": "Shiferaw", "email": "yostina@example.com",
     "password": "password123"},
    {"username": "lifetf", "name": "Life", "surname": "Tafere", "email": "life@example.com", "password": "password123"},
    {"username": "gulsezimbg", "name": "Gulsezim", "surname": "Bigali", "email": "gulsezim@example.com",
     "password": "password123"},
    {"username": "zakirhs", "name": "Zakir", "surname": "Huseynov", "email": "zakir@example.com",
     "password": "password123"}
]


# Add data to the database
def populate_database():
    with app.app_context():
        # Add users
        for user_data in users:
            password_hash = generate_password_hash(user_data["password"], method="pbkdf2:sha256", salt_length=8)
            user = User(
                username=user_data["username"],
                name=user_data["name"],
                surname=user_data["surname"],
                email=user_data["email"],
                password=password_hash
            )
            db.session.add(user)

        # Add animals
        for animal_data in animals:
            animal = Animal(
                user_id=animal_data["user_id"],
                animal_name=animal_data["animal_name"],
                animal_type=animal_data["animal_type"],
                animal_gender=animal_data["animal_gender"],
                animal_age=animal_data["animal_age"],
                animal_color=animal_data["animal_color"],
                history=animal_data.get("history"),
                character=animal_data.get("character"),
                behavioral_features=animal_data.get("behavioral_features"),
                preferences=animal_data.get("preferences"),
                image_url=animal_data.get("image_url")  # Assume image_url is a valid URL for the animal image
            )
            db.session.add(animal)

        db.session.commit()
        print("Database populated with expanded animal data.")


# Run the function to populate the database
populate_database()
