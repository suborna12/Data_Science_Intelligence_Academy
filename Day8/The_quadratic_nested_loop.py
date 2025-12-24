lst_a = [1, 2, 3, 6, 9, 11]
lst_b = [6, 7, 8, 9, 10, 11]
dpl = []
for i in lst_a:
    for j in lst_b:
        if i == j:
            dpl.append(i)
    
print(f"Duplicates numbers are: {dpl}")
