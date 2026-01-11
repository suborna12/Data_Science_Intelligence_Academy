def A(func):
    def wrapper():
        print("Inside A before call")
        result  = func()
        print("Inside A after call")
        return result
    return wrapper

def B(func):
    def wrapper():
        print("Inside B before call")
        result = func()
        print("Inside B after call")
        return result
    return wrapper

@A
@B
def new_f():
    print("Original Function")

new_f() 