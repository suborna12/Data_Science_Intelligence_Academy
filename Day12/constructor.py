class User:
    def __init__(self, username):
        self.name = username
        self.is_active = True


user_obj = User.__new__(User)
User.__init__(user_obj, "Alice")
print(user_obj.name)       
print(user_obj.is_active)  
