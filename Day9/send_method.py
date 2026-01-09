def generator():
    current_val = 0
    while True:
        val = yield current_val
        
        if val is not None:
            current_val = val
        else:
            current_val += 1

gen = generator()
print(next(gen)) 
print(gen.send(10)) 
print(next(gen))
