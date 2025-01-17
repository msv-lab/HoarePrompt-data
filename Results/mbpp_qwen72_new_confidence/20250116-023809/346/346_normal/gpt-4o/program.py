def new_tuple(input_list, input_string):
    return tuple(input_list) + (input_string,)

# Test cases
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
