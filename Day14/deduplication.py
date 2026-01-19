def remove_duplicates(lst):
    seen = set()
    r = []
    for i in lst:
        if i not in seen:
            seen.add(i)
            r.append(i)
    return r

nums = [1, 2, 3, 4, 5, 4, 2, 6, 7, 1]
print(remove_duplicates(nums))