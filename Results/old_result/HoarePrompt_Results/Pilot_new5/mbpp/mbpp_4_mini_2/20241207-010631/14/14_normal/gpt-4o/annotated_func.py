#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all unique integers from `arr`. If there are no duplicates in `arr`, the loop will execute for every integer in `arr` and `num` will be the last integer in `arr`. If there are duplicates, the loop will stop executing upon encountering the first duplicate integer.
    return False
    #The program returns False, indicating that there is at least one duplicate integer in the list 'arr'.
#Overall this is what the function does:The function accepts a list of integers and returns True if there are any duplicate integers in the list; otherwise, it returns False if all integers are unique.

