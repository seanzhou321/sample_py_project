from sample_project.models.user import User
from sample_project.services.user_service import UserService
from sample_project.utils.validators import EmailValidator
from sample_project.resource_loader import ResourceLoader

# Allo imports directly from package root without needing the full package path
# i.e.
# from sample_project import User, UserService, EmailValidator
__all__ = ['User', 'UserService', 'EmailValidator', 'ResourceLoader']

# Package-level configuration
# VERSION = '1.0.0'
# AUTHOR = 'Your Name'
#
# def get_version(): 
#   return VERSION

# Usage
# from sample_project import VERSION, get_version