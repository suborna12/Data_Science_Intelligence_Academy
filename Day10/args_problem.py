def wrapper(func):
    def timer(*args, **kwargs):
        print("Logging...")
        return func(*args, **kwargs)
    return timer

@wrapper
def add(a, b):
    return a + b

print(add(3, 4))