def string_to_list(s: str) -> list:
    return s.split()

# Test cases
assert string_to_list("python programming") == ['python', 'programming']
assert string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
assert string_to_list("write a program") == ['write', 'a', 'program']
