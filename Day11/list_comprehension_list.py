lst = [1, 2, 3, 4, 5]
mp_lmd = list(map(lambda x: x * x, lst))
lst_cmp = [x * x for x in lst]
print(f"Result of map + lamba: ", (mp_lmd))
print(f"Result of list comprehension: ", lst_cmp)