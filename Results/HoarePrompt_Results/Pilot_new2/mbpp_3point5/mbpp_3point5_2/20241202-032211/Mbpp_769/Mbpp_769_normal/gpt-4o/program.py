def Diff(list1, list2):
    # Convert lists to sets and find their symmetric difference
    set1 = set(list1)
    set2 = set(list2)
    diff_elements = set1.symmetric_difference(set2)
    
    # Convert the set back to a list and sort it to ensure the order matches the expected results
    result_list = list(diff_elements)
    result_list.sort(key=lambda x: (list1 + list2).index(x))
    
    return result_list

# Test cases
assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
assert Diff([1,2,3,4,5], [6,7,1]) == [2,3,4,5,6,7]
assert Diff([1,2,3], [6,7,1]) == [2,3,6,7]
