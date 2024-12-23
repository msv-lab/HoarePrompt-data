#State of the program right berfore the function call: arr is a list of elements, and element is a value of the same type as the elements in arr.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list with at least one element, `index` is the index of the last checked element in the list, `value` is the last element checked in the list, and if `element` is found in the list, the function returns `True` and `index`. If `element` is not found, the function returns `False` and `index` remains the index of the last checked element.
    return False, -1
    #The program returns False and index that remains the index of the last checked element
#Overall this is what the function does:The function `func_1` accepts a list `arr` and a value `element`. It iterates through the list to check if `element` matches any of the elements in `arr`. If a match is found, it returns `True` along with the index of the matching element. If no match is found, it returns `False` along with the index of the last checked element. The function covers all possible outcomes where the `element` is either found at index 0, 1, or 2, or not found, in which case it returns `False` and the index of the last checked element.

