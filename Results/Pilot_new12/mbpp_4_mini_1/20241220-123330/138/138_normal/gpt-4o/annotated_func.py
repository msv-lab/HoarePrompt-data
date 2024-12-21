#State of the program right berfore the function call: arr is a list of elements, and element can be of any type.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements; if `element` is found in `arr`, the loop will return True along with the corresponding `index`, which is the position of `element` in `arr`. If `element` is not found after all iterations, the loop will not return anything, and `index` will be equal to the length of `arr` (indicating the number of elements traversed).
    return False, -1
    #The program returns False indicating that `element` is not found in `arr`, and -1 indicating that there is no valid index for `element`.
#Overall this is what the function does:The function accepts a list `arr` and an `element`. It checks if `element` is present in the list `arr`. If found, it returns `True` along with the index of the first occurrence of `element`. If `element` is not found in `arr` after checking all elements, it returns `False` and -1 to indicate that `element` is not present. The function handles all elements in the list, regardless of their type, and correctly accounts for cases where the list is empty or where the `element` is not present at all. There are no restrictions on the index range, with the function correctly identifying the absence of the element by returning -1.

