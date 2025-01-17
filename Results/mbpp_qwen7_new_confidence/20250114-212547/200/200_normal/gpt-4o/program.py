def extract_string(strings, size):
    return [string for string in strings if len(string) == size]

# Tests
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8) == ['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6) == ['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9) == ['exercises']
