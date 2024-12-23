#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all unique elements of `arr`, the function returns either `True` if any duplicate is found or `None` if no duplicates are found.
    return False
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks for the presence of any duplicate elements within the list. If a duplicate is found during the iteration, the function immediately returns `True`. If no duplicates are found after checking all elements, the function returns `False`. There are no additional side effects or changes to the input list `arr`. The function does not modify the input list `arr` and only returns a boolean value indicating whether duplicates were found.

