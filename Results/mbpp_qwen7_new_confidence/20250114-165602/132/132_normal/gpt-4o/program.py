def rear_extract(tuples_list):
    return [tup[-1] for tup in tuples_list]

# Testing the function with provided test cases
assert rear_extract([(1, 'Rash', 21)]) == [21]
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]

print("All test cases passed!")
