#State of the program right berfore the function call: array is a list of elements, and element is a value that can be compared with the elements in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the index which is the position of element in array
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: array is a list of elements, and element is a value. If element is found in array, the function returns True and the index of element, otherwise, it returns False and -1.
#Overall this is what the function does:The function accepts a list `array` and a value `element`, and returns a tuple. The first element of the tuple is `True` if `element` is found in `array`, and `False` otherwise. The second element of the tuple is the index of `element` in `array` if it is found, or `-1` if not found. This function handles the case where `element` is not in `array` but does not explicitly handle cases where `array` is not a list or where `element` appears multiple times in `array`.

