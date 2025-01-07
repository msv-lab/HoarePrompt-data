#State of the program right berfore the function call: arr is a list of elements, and element can be of any data type.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements, `element` is the value being searched for in `arr`. If the element is found, the output is `True` and the index of the first occurrence; otherwise, the loop does not execute and no value is returned, with the original `arr` remaining unchanged.
    return False, -1
    #The program returns False, indicating that the element is not found in the list 'arr', and -1, indicating that there is no valid index for the first occurrence.
#Overall this is what the function does:The function accepts a list `arr` and an element of any data type. It searches for the first occurrence of `element` in `arr`. If found, it returns `True` and the index of the first occurrence; if not found, it returns `False` and -1. This means the function has a straightforward mechanism for indicating the presence or absence of an element and its position, covering all potential cases without any missing logic.

