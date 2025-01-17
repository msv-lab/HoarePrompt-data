from collections import Counter

def two_unique_nums(lst):
    # Count the occurrences of each number in the list
    count = Counter(lst)
    
    # Filter out the numbers that occur more than once
    result = [num for num in lst if count[num] == 1]
    
    return result

# Testing the function with the provided test cases
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
