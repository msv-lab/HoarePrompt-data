def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
    return True
assert func_1(['green', 'orange', 'black', 'white'], 'blue') == False
assert func_1([1, 2, 3, 4], 7) == False
assert func_1(['green', 'green', 'green', 'green'], 'green') == True