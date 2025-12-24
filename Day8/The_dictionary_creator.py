def build_dict_from_list(lst):
    new_dict = {}  

    for item in lst:
        hash_value = hash(item)  
        new_dict[hash_value] = item  

    return new_dict

lst = ["Shashanka", "Suborna", "Shuvo", "Simanto", "Sujothna"]
result = build_dict_from_list(lst)
print(f"After processing {result}")
