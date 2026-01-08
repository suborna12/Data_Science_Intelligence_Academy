def set_contains(set, target):
    index = hash(target) % len(set)
    return target in set[index]



set = [[] for _ in range(2000)]

for i in range(-1000, 1000):
    index = hash(i) % len(set)
    set[index].append(i)

print(set_contains(set, -5))
