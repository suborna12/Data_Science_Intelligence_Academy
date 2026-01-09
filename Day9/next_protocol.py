def gen():
    yield 1
    yield 2
    yield 3

a = gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))