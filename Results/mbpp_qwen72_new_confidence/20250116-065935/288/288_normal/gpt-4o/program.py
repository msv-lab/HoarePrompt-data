def sample_nam(names):
    # Filter out names that start with a lowercase letter
    filtered_names = [name for name in names if not name[0].islower()]
    # Sum the lengths of the remaining names
    total_length = sum(len(name) for name in filtered_names)
    return total_length

# Tests
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"]) == 10
assert sample_nam(["abcd", "Python", "abba", "aba"]) == 6
