class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def save(self):
        # Logic to save the user to the database
        pass

    def delete(self):
        # Logic to delete the user from the database
        pass

    def update(self):
        # Logic to update the user information in the database
        pass

    @classmethod
    def find_by_id(cls, user_id):
        # Logic to find a user by their ID
        pass

    @classmethod
    def find_by_username(cls, username):
        # Logic to find a user by their username
        pass

    @classmethod
    def find_all(cls):
        # Logic to retrieve all users from the database
        pass