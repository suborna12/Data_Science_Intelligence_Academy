def repeat_factory(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator


@repeat_factory(3)
def process():
    print("Processing...")


process()