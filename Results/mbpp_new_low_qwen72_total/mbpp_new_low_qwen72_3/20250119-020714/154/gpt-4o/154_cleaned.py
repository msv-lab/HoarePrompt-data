def func_1(d):
    if not isinstance(d, dict) or not d:
        return 1
    else:
        return 1 + max((func_1(value) for value in d.values()))
assert func_1({'a': 1, 'b': {'c': {'d': {}}}}) == 4
assert func_1({'a': 1, 'b': {'c': 'python'}}) == 2
assert func_1({1: 'Sun', 2: {3: {4: 'Mon'}}}) == 3