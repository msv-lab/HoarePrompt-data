def odd_position(lst):
    # Iterate through the list, checking only elements at odd indices
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

# Testing the function with the provided test cases
assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True
assert odd_position([4, 1, 2]) == True
assert odd_position([1, 2, 3]) == False
