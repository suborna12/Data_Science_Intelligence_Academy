import sys
a = [x for x in range(1000000)]
b = (x for x in range(1000000))

print("size of a: " ,sys.getsizeof(a))
print("size of b: " ,sys.getsizeof(b))