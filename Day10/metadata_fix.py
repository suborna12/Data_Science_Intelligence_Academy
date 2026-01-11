import functools

def decorator(original):
    @functools.wraps(original)
    def copy_metadata ( wrapper ):
        wrapper.__name__ = original.__name__
        wrapper.__doc__ = original.__doc__
        return wrapper()
    return copy_metadata


@decorator
def my_function():
    """Original function"""
    print("Hello")


print(my_function.__name__)
print(my_function.__doc__)