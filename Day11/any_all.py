lst = [1, 2, -3, 4, 5, -4, 7, -9]
any_neg = any(x < 0 for x in lst)
all_pos = all(x > 0 for x in lst)
print("Checking any of numbers are negative: ", (any_neg))
print("Checking all of numbers are positive : ", (all_pos))