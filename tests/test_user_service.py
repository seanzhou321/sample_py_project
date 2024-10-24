# tests/test_user_service.py
import pytest
from sample_project.services.user_service import UserService
from sample_project.models.user import User

@pytest.fixture
def user_service():
    """Fixture to create a UserService instance for tests"""
    return UserService()

@pytest.fixture
def valid_user_data():
    """Fixture for valid user test data"""
    return {
        "username": "john_doe",
        "email": "john@example.com"
    }

def test_create_user_success(user_service, valid_user_data):
    """Test successful user creation"""
    user = user_service.create_user(
        valid_user_data["username"],
        valid_user_data["email"]
    )
    
    assert isinstance(user, User)
    assert user.username == valid_user_data["username"]
    assert user.email == valid_user_data["email"]
    assert user.is_active == True

def test_create_user_invalid_email(user_service):
    """Test user creation with invalid email"""
    with pytest.raises(ValueError) as exc_info:
        user_service.create_user("john_doe", "invalid-email")
    
    assert "Invalid email format" in str(exc_info.value)

def test_get_user_info(user_service, valid_user_data):
    """Test getting user info"""
    user = user_service.create_user(
        valid_user_data["username"],
        valid_user_data["email"]
    )
    
    info = user_service.get_user_info(user)
    
    assert info == {
        "username": valid_user_data["username"],
        "email": valid_user_data["email"],
        "status": "active"
    }

@pytest.mark.parametrize("email,is_valid", [
    ("test@example.com", True),
    ("user@domain.co.uk", True),
    ("invalid-email", False),
    ("test@", False),
    ("@domain.com", False),
])
def test_email_validation(user_service, email, is_valid):
    """Test email validation with various email formats"""
    if is_valid:
        user = user_service.create_user("username", email)
        assert user.email == email
    else:
        with pytest.raises(ValueError):
            user_service.create_user("username", email)