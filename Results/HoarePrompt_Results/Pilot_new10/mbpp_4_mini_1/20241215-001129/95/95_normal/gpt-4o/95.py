def count_occurance(s: str) -> int:
    return s.count('std')

# Test cases to validate the solution
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2
assert count_occurance("stds") == 1
assert count_occurance("") == 0
