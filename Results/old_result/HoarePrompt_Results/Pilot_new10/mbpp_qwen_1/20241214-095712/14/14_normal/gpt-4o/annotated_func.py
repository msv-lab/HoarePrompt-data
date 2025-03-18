#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all integers from `arr`, and the function returns `False` if no duplicate was found in `arr`.
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a list of integers and returns True if any duplicate is found, otherwise it returns False.

