def is_Sub_Array(main_list, sub_list):
    """
    Check if sub_list is a sublist of main_list.

    :param main_list: List of integers
    :param sub_list: List of integers to check as sublist
    :return: Boolean indicating if sub_list is a sublist of main_list
    """
    if not sub_list:  # An empty list is always a sublist
        return True
    
    len_main = len(main_list)
    len_sub = len(sub_list)
    
    # Iterate through the main list to see if we can find the sub_list
    for i in range(len_main - len_sub + 1):
        if main_list[i:i+len_sub] == sub_list:
            return True
    
    return False

# Test cases
assert is_Sub_Array([1,4,3,5],[1,2]) == False
assert is_Sub_Array([1,2,1],[1,2,1]) == True
assert is_Sub_Array([1,0,2,2],[2,2,0]) == False
