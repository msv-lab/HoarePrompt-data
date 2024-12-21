def func_1(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
assert func_1((['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange'])) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
assert func_1(([' red ', 'green'], ['blue ', ' black'], [' orange', 'brown'])) == [[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
assert func_1((['zilver', 'gold'], ['magnesium', 'aluminium'], ['steel', 'bronze'])) == [['gold', 'zilver'], ['aluminium', 'magnesium'], ['bronze', 'steel']]