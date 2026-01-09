def gen():
    yield 1
    yield 2
    yield 3
a = gen()

for i in a:
    print(a)

print("After Second time loop: ")

for i in a:
    print(a)