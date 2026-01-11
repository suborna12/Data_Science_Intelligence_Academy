def my_decorator(func):
    def wrapper():
        print("Before Call")
        func()
        print("After Call")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello() 
