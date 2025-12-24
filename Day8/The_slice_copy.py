def slice_list(source, k):
    new_list = [None] * k  
    for i in range(k):
        new_list[i] = source[i]
    return new_list

list_n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = slice_list(list_n, 5)
print(result)  
