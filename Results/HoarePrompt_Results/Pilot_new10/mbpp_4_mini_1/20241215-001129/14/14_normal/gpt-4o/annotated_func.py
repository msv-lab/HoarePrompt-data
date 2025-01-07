#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all unique integers from `arr`.
    return False
    #The program returns False indicating a condition was not met, regardless of the contents of 'arr' or 'seen'.
#Overall this is what the function does:The function accepts a list of integers and returns True if any integer appears more than once; otherwise, it returns False, including for the case of an empty list which also returns False.

