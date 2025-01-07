def extract_rear(tup):
    return [s[-1] for s in tup]

# Test cases
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
assert extract_rear(('Avenge', 'for', 'People')) == ['e', 'r', 'e']
assert extract_rear(('Gotta', 'get', 'go')) == ['a', 't', 'o']
