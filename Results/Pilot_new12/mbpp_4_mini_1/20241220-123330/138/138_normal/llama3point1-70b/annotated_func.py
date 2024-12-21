#State of the program right berfore the function call: array is a list of elements, and element can be any type.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True along with the index which is the position of element in the array.
    except (ValueError):
        return False, -1
        #The program returns a tuple (False, -1)
    #State of the program after the try-except block has been executed: `array` is a list of elements which can be of any type. If the `element` is found, the function returns (True, index) where index is the position of element in the array; otherwise it returns (False, -1).
#Overall this is what the function does:The function accepts a list `array` and an `element`. It attempts to find the index of `element` in `array`. If `element` is found, the function returns a tuple (True, index), where `index` is the position of `element` in `array`. If `element` is not found, a ValueError is raised and the function returns (False, -1). The function handles cases where the input `array` could be empty or contain elements of any type. There are no specific validations on the types of `array` or `element`, which means it can raise an error if `array` is not a list or if an operation is performed on unsupported types. Therefore, the final state indicates that the program outputs a boolean indicating presence and the corresponding index or a failure signal.

