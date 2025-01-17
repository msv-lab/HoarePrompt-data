def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    else:
        return 1 + max(dict_depth(value) for value in d.values())

# Test cases
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c':'python'}}) == 2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}}) == 3
