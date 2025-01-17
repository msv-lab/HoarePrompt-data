def is_sublist(main_list, sublist):
    len_main = len(main_list)
    len_sub = len(sublist)
    
    # If the sublist is empty or larger than the main list, return False
    if len_sub == 0 or len_sub > len_main:
        return False
    
    # Iterate through the main list
    for i in range(len_main - len_sub + 1):
        # Check if the sublist matches the slice of the main list
        if main_list[i:i + len_sub] == sublist:
            return True
    
    return False

# Tests
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
assert is_sublist([2, 4, 3, 5, 7], [4, 3]) == True
assert is_sublist([2, 4, 3, 5, 7], [1, 6]) == False
