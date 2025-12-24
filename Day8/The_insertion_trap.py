def insert_at_zero(list, new_value):
    n = len(list)
    list.append(None)
    for i in range(n, 0, -1):
        list[i] = list[i - 1]  

    list[0] = new_value

lst = [1, 2, 3, 4, 5]
insert_at_zero(lst, 99)
print(f"After using insert function {lst}")
lst.append(98)
print(f"After using append {lst}")
