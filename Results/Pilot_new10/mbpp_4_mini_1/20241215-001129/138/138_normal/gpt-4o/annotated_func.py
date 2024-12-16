#State of the program right berfore the function call: arr is a list and element can be of any data type.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list that may contain any data type, `element` is the value being searched for, and the loop returns True and the index of the first occurrence of `element` if it exists in `arr`; otherwise, it returns None if the `element` is not found in the list.
    return False, -1
    #The program returns False and -1, indicating that the element is not found in the list `arr`.
#Overall this is what the function does:The function accepts a list `arr` and a value `element`. It searches for the first occurrence of `element` in `arr` and returns `True` along with the index of the first occurrence if found; otherwise, it returns `False` and -1. The function does not limit the search to the first three indices, contrary to what is stated in the annotations.

