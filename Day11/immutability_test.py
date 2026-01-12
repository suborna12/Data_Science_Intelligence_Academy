def impure(lst):
    lst[0] = 99
    return lst

def pure(lst):
    new_lst = lst.copy()
    lst[0] = 99
    return new_lst
