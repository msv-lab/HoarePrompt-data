def consecutive_duplicates(lst):
    if not lst:
        return []

    # Initialize the result list with the first element
    result = [lst[0]]

    # Iterate over the list starting from the second element
    for i in range(1, len(lst)):
        # If the current element is different from the last element in result, append it
        if lst[i] != lst[i - 1]:
            result.append(lst[i])

    return result

# Testing the function with the provided test cases
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [10, 15, 19, 18, 17, 26, 17, 18, 10]
assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd']) == ['a', 'b', 'c', 'd']
assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd', 'a', 'a']) == ['a', 'b', 'c', 'd', 'a']
