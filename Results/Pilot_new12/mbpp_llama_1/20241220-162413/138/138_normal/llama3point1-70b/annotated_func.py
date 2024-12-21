#State of the program right berfore the function call: array is a list of elements, and element is any type of object that can be compared for equality with elements in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True and the index of the first occurrence of 'element' in 'array'
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: array is a list of elements, and element is any type of object that can be compared for equality with elements in the array. If the element is found in the array, the function returns True and the index of the element, otherwise, it returns False and -1.
#Overall this is what the function does:The function `func_1` checks if a given `element` exists in a provided `array` and returns a boolean indicating whether the element was found along with the index of the element if found, or -1 if not found. The function handles the case where the `element` is not present in the `array` by catching a `ValueError` exception and returning `False` along with -1. The original state of the `array` and `element` remains unchanged after the function execution, regardless of whether the `element` is found or not. The function does not modify the input `array` or `element` in any way and only performs a search operation. The return values are either `True` and the index of the first occurrence of `element` in `array`, or `False` and -1 if `element` is not found. The function handles edge cases where the `array` is empty or the `element` is not comparable for equality, implicitly handling these cases through the `index()` method's behavior and exception handling.

