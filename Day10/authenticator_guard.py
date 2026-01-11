g_user = "admin"
def auth_decorator(func):
    def auth_wrapper():
        if g_user != "admin":  
            raise PermissionError("Access Denied")
        return func()
    return auth_wrapper

@auth_decorator
def new_f():
    print("This is Admin")

new_f()
