def nums():
    for i in range(1, 11):
        yield i

def square(numbers):
    for n in numbers:
        yield n * n

def even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

pipeline  = even(square(nums()))

for i in pipeline:
    print(i)