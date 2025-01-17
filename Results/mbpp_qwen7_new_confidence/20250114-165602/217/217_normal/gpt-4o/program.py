def tuple_intersection(list1, list2):
    # Convert each tuple to a sorted tuple for both lists
    set1 = {tuple(sorted(t)) for t in list1}
    set2 = {tuple(sorted(t)) for t in list2}
    
    # Find the intersection of two sets
    intersection = set1 & set2
    
    return intersection

# Tests
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)], [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)], [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}
