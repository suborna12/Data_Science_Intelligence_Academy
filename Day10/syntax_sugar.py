def timer(func):
    def wrapper():
        print("Before Calling")
        func()
        print("After Calling")
    return wrapper

@timer
def say_hello():
    pass

say_hello()