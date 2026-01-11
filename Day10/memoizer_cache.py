def memoize(func):
    cache = {}  
    
    def wrapper(n):
        if n in cache:
            return cache[n]  

        val = func(n)        
        cache[n] = val       
        return val          

    return wrapper

@memoize
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(10))