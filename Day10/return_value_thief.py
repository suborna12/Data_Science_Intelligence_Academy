def decorator(func):
    def wrapper():
        return func()
    return wrapper

@decorator
def new_f():
    print("Null")

new_f()