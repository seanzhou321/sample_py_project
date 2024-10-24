from sample_project.services.user_service import UserService

# Create a new user service
service = UserService()

# Create a new user
user = service.create_user("alice", "alice@example.com")

# Get user info
info = service.get_user_info(user)
print(info)
# Output: {'username': 'alice', 'email': 'alice@example.com', 'status': 'active'}