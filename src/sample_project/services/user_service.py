from sample_project.models.user import User
from sample_project.utils.validators import EmailValidator

class UserService:
    def __init__(self):
        self.validator = EmailValidator()
    
    def create_user(self, username, email):
        if not self.validator.is_valid_email(email):
            raise ValueError("Invalid email format")
        
        user = User(username, email)
        return user.activate()
    
    def get_user_info(self, user):
        return {
            "username": user.username,
            "email": user.email,
            "status": "active" if user.is_active else "inactive"
        }