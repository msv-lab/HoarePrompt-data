#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing unique integers from `arr` up to the point where either all numbers have been processed or a duplicate is found, and if a duplicate is found, the function returns `True`. If `arr` is empty, `seen` remains an empty set.
    return False
    #The program returns False, indicating that no duplicate was found in the list `arr`, and the set `seen` contains unique integers from `arr`
#Overall this is what the function does:The function accepts a list of integers `arr` and returns a boolean value indicating whether there are duplicate integers in the list. If a duplicate is found, the function immediately returns `True`. If no duplicates are found after processing all numbers in the list, the function returns `False`. The function handles edge cases such as an empty list, in which case it returns `False`. Additionally, the function only considers the presence of duplicate integers and does not modify the original list `arr`. The function's return value can be used to determine the presence or absence of duplicates in the input list.

