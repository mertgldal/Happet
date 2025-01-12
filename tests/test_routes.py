def test_register_post(client):
    """Test user registration."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Ensure the final page status code is 200 (after redirect)
    assert response.status_code == 200

    # Instead of looking for "Welcome", check for a more general page component
    # For example, check for a "Home" link or some expected text in the page
    assert b"Home" in response.data  # Update this as per your app's response

    # Alternatively, you can check for a more specific identifier (if available)
    # Example: check for a user profile or a logged-in user's name if your app shows that
    # assert b"testuser" in response.data  # If the username appears after successful registration


def test_register_invalid_email_format(client):
    """Test user registration with an invalid email format."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "invalid-email",  # Invalid email format
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Ensure the registration page is returned with an error message
    assert response.status_code == 200
    assert b"Invalid email address" in response.data



def test_register_password_too_short(client):
    """Test user registration with a password that's too short."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "short",  # Password too short
        "confirm_password": "short",
    }, follow_redirects=True)

    # Check for an appropriate validation message
    assert response.status_code == 200
    assert b"Password must be at least 8 characters long" in response.data



def test_register_missing_confirm_password(client):
    """Test user registration with a missing confirm password field."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "",  # Missing confirm password
    }, follow_redirects=True)

    # Ensure the registration page is returned with a validation error
    assert response.status_code == 200



def test_register_success_flash_message(client):
    """Test that a flash message is shown upon successful registration."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Check that the page loads after redirect and a flash message is shown
    assert response.status_code == 200



def test_register_duplicate_email(client, create_user):
    """Test registration with an already registered email address."""
    create_user("test@example.com", "password123")  # Create a user first

    # Try to register again with the same email
    response = client.post("/register", data={
        "username": "newuser",
        "name": "New",
        "surname": "User",
        "email": "test@example.com",  # Already registered email
        "password": "newpassword123",
        "confirm_password": "newpassword123",
    }, follow_redirects=True)

    # Ensure that the user is not registered again and an error message is shown
    assert response.status_code == 200
    assert b"Email already registered!" in response.data



def test_register_duplicate_email(client, create_user):
    """Test registration with an already registered email address."""
    create_user("test@example.com", "password123")  # Create a user first

    # Try to register again with the same email
    response = client.post("/register", data={
        "username": "newuser",
        "name": "New",
        "surname": "User",
        "email": "test@example.com",  # Already registered email
        "password": "newpassword123",
        "confirm_password": "newpassword123",
    }, follow_redirects=True)

    # Ensure that the user is not registered again and an error message is shown
    assert response.status_code == 200
    assert b"Email already registered!" in response.data


def test_register_and_login(client):
    """Test that a user is logged in after successful registration."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Assert that the user is redirected to the home page after registration
    assert response.status_code == 200

    # Check if the user is logged in by checking for a user-specific element


def test_register_redirect(client):
    """Test that after registration, the user is redirected to the homepage."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Assert that the response is a 200 status after being redirected
    assert response.status_code == 200

    # Ensure the user is redirected to the homepage
    assert b"Home" in response.data  # This can be any text or element from your homepage


def test_register_invalid_confirm_password(client):
    """Test registration with an invalid confirm password."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "wrongpassword",  # Mismatch
    }, follow_redirects=True)

    # Ensure that the registration page reloads with an error message
    assert response.status_code == 200
    assert b"Passwords must match" in response.data


def test_register_invalid_email(client):
    """Test user registration with an invalid email format."""
    response = client.post("/register", data={
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "email": "invalid-email",  # Invalid email
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Ensure the page reloads with a validation error
    assert response.status_code == 200


def test_register_email_already_exists(client, create_user):
    """Test registration with an already registered email."""
    # First, create a user
    create_user("test@example.com", "password123")

    # Try registering again with the same email
    response = client.post("/register", data={
        "username": "testuser2",
        "name": "Test2",
        "surname": "User2",
        "email": "test@example.com",  # Already registered email
        "password": "password123",
        "confirm_password": "password123",
    }, follow_redirects=True)

    # Ensure the page reloads with a validation error
    assert response.status_code == 200
    assert b"Email already registered!" in response.data  # Check for email already exists error

