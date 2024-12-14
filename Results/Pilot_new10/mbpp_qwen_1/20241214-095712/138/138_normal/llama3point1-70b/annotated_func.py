#State of the program right berfore the function call: array is a list of elements, and element is a value to search within the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and index, where index is the index of element in array
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: The function returns a tuple (boolean, integer). If `element` is found in `array`, the function returns (True, index), where `index` is the position of `element` in `array`. If `element` is not found in `array`, the function returns (False, -1).
#Overall this is what the function does:The function `func_1` accepts a list `array` and a value `element`. It searches for `element` in `array` and returns a tuple `(boolean, integer)`. If `element` is found, it returns `(True, index)` where `index` is the position of `element` in `array`. If `element` is not found, it returns `(False, -1)`.

