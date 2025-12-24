def contains(list, target):
    index = 0
    length = len(list)
    while index < length:
        current_value = list[index]
        if current_value == target:
            return True
        index += 1
    return False


list_n = list(range(-1000, 1000))
print(contains(list_n, -5))