def flatt(lst):
    r = []
    for i in lst:
        if isinstance(i, list):
            r.extend(flatt(i))
        else:
            r.append(i)
    return r


print(flatt([1, [2, [3, 4], 5], 6]))
