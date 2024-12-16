#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing unique integers from `arr` up to the point where a duplicate is found or all integers if no duplicates are found, and the function returns `True` if a duplicate is found or completes normally if no duplicates are found.
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a list of integers, checks for duplicates, and returns True if any duplicates are found, or False if the list contains all unique integers or is empty.

