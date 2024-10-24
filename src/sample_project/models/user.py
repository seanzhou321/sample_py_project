class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = False
    
    def activate(self):
        self.is_active = True
        return self