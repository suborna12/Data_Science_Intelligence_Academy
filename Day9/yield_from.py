def gen1():
    yield 1
    yield 2
    yield 3
def gen2():
    yield 4
    yield 5
    yield 6

def combined():
    yield from gen1()
    yield from gen2()

for i in combined():
    print(i)