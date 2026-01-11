import time
def timer(func):
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()   
        result = func(*args, **kwargs)     
        end_time = time.perf_counter()
        print(end_time - start_time)
        return result
    return timer_wrapper
@timer
def process_data(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(process_data(10))
