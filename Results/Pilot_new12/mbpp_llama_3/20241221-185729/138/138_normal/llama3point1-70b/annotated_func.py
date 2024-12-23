#State of the program right berfore the function call: array is a list of elements, and element is a value that can be compared to the elements in the array for equality.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the 0-indexed position of 'element' in 'array'
    except (ValueError):
        return False, -1
        #The program returns a boolean value False and an integer -1
    #State of the program after the try-except block has been executed: array is a list of elements and element is a value compared to the elements in the array for equality. The function returns True and the 0-indexed position of 'element' in 'array' if 'element' exists in 'array', otherwise it returns False and -1.
#Overall this is what the function does:The function `func_1` checks if a given `element` exists in a provided `array`, returning a boolean value indicating the presence of the element and its 0-indexed position if found, or -1 if not found. It handles the case where the `element` is not in the `array` by catching the `ValueError` exception raised by the `index` method, ensuring the function does not crash and instead returns a predictable result. The function does not modify the input `array` or `element` in any way, making it a read-only operation. The return values are a tuple containing a boolean (`True` if the element is found, `False` otherwise) and an integer (the index of the element if found, -1 if not found). The function's behavior is deterministic, meaning it will always return the same output given the same inputs, including handling edge cases such as an empty input array or a `None` input for either parameter, although these cases are not explicitly annotated, the function's code implies it can handle them by either returning `False` and `-1` for `None` or an empty array, or potentially throwing an exception if the inputs are not of the expected types.

