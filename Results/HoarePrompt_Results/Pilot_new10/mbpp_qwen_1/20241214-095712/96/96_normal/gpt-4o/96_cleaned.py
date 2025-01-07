def func_1(tup):
    if not tup:
        return True
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
    return True
assert func_1((5, 6, 7, 3, 5, 6)) == True
assert func_1((1, 2, '4')) == False
assert func_1((3, 2, 1, 4, 5)) == True