#State of the program right berfore the function call: arr is a list, and element can be of any data type.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list, `index` is the index of the first occurrence of `element` in `arr` if it exists, otherwise `index` is the length of `arr`, and `value` is the element at that index if `element` is found, otherwise `value` is not defined. If `element` is not present in `arr`, the loop executes for every element in `arr`. If `arr` is empty, the loop does not execute, and `index` is 0.
    return False, -1
    #The program returns False and -1, indicating that the element was not found in the list `arr`.
#Overall this is what the function does:The function accepts a list `arr` and an `element`. It searches for the first occurrence of the `element` in the list and returns `True` along with its index if found. If the `element` is not found in the list, it returns `False` and -1. The function does not limit the search to the first three positions as stated in the annotations; it checks the entire list. If the list `arr` is empty, it directly returns `False` and -1.

