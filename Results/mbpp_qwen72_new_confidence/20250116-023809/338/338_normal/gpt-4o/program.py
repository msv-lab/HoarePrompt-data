def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    
    packed_list = []
    current_sublist = [lst[0]]
    
    for elem in lst[1:]:
        if elem == current_sublist[-1]:
            current_sublist.append(elem)
        else:
            packed_list.append(current_sublist)
            current_sublist = [elem]
    
    packed_list.append(current_sublist)
    return packed_list

# Test cases
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd']) == [['a', 'a'], ['b'], ['c'], ['d', 'd']]
