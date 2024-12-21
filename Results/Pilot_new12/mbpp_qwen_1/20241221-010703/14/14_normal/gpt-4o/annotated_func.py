#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)
        
    #State of the program after the  for loop has been executed: `arr` is a list of integers, `seen` is a set containing all integers from `arr`, and the loop has either returned `True` if any integer was repeated or continued until all integers were processed without returning.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns `True` if any integer in the list is duplicated, otherwise it returns `False`. After processing the list, the function ensures that no integer is repeated more than once. If a duplicate is found during iteration, the function immediately returns `True`. If the loop completes without finding any duplicates, the function returns `False`. The function handles edge cases such as an empty list or a list with a single element by ensuring these scenarios do not falsely trigger a duplicate detection.

