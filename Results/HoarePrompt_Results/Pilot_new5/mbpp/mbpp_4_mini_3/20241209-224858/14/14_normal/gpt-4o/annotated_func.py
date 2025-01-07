#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all unique integers from `arr`, the loop returns True if any integer in `arr` is duplicated, otherwise it returns False after checking all elements.
    return False
    #The program returns False, indicating that there are no duplicated integers in the list 'arr' since all integers in 'arr' are unique as evidenced by the 'seen' set.
#Overall this is what the function does:The function accepts a list of integers `arr` and checks for duplicate integers. It returns True if any integer is duplicated within the list; otherwise, it returns False if all integers are unique.

