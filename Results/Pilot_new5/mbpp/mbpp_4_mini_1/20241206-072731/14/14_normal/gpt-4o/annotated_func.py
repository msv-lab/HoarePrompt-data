#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all unique integers from `arr`. If there are no duplicates in `arr`, the loop executes for all integers in `arr`. If there are duplicates, the loop terminates early upon finding the first duplicate, and `seen` will contain all integers up to (but not including) the first duplicate.
    return False
    #The program returns False, indicating that there is a duplicate in the list 'arr', as the loop terminates early upon finding the first duplicate.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns True if there are any duplicate integers in the list; otherwise, it returns False.

