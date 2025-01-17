def union_elements(tup1, tup2):
    # Step 1: Convert tuples to sets
    set1 = set(tup1)
    set2 = set(tup2)
    
    # Step 2: Find the union of the sets
    union_set = set1 | set2
    
    # Step 3: Convert the union set to a sorted list
    sorted_list = sorted(union_set)
    
    # Step 4: Convert the sorted list to a tuple and return
    return tuple(sorted_list)

# Provided test cases
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
assert union_elements((1, 2, 3, 4),(3, 4, 5, 6)) == (1, 2, 3, 4, 5, 6)
assert union_elements((11, 12, 13, 14),(13, 15, 16, 17)) == (11, 12, 13, 14, 15, 16, 17)
