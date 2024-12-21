def func_1(tup):
    return [s[-1] for s in tup]
assert func_1(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
assert func_1(('Avenge', 'for', 'People')) == ['e', 'r', 'e']
assert func_1(('Gotta', 'get', 'go')) == ['a', 't', 'o']