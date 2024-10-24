import re

class EmailValidator:
    def __init__(self):
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    def is_valid_email(self, email):
        return bool(re.match(self.email_pattern, email))