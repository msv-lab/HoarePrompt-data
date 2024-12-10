#State of the program right berfore the function call: arr is a list of elements, and element can be of any type that is comparable with the elements in arr.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements, `element` is a value that may or may not be present in `arr`, `index` is the index of `element` in `arr` if found, or equal to the length of `arr` if `element` is not in `arr`, and `value` is equal to `element` if found, or None if it is not present. If the list is empty, `index` is 0 and `value` is None.
    return False, -1
    #The program returns False and -1, indicating that the element is not present in the array
#Overall this is what the function does:The function accepts a list `arr` and a comparable `element`. It returns `True` and the index of the first occurrence of `element` in `arr` if found; otherwise, it returns `False` and -1. If `arr` is empty, it will return `False` and -1 as well. The function does not raise any exceptions for incorrect input types but assumes that the `element` is comparable to the elements in `arr`.

