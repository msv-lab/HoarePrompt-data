def check_Consecutive(lst):
    if not lst:  # If the list is empty, it cannot be consecutive
        return False
    
    lst_sorted = sorted(lst)
    
    for i in range(len(lst_sorted) - 1):
        if lst_sorted[i + 1] - lst_sorted[i] != 1:
            return False
    
    return True

# Test cases
assert check_Consecutive([1, 2, 3, 4, 5]) == True
assert check_Consecutive([1, 2, 3, 5, 6]) == False
assert check_Consecutive([1, 2, 1]) == False
