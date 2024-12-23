#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all integers from `arr` that were encountered during the loop, and the function returns `True` if any duplicate integer is found in `arr`. Otherwise, the function returns `False`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks for the presence of any duplicate integers within the list. It maintains a set called `seen` to track the integers it encounters. If a duplicate integer is found, the function returns `True`. If no duplicates are found after iterating through the entire list, the function returns `False`. The function covers all edge cases, including an empty list where no duplicates can exist, and a list with only unique elements.

