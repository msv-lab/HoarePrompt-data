#State of the program right berfore the function call: array is a list of elements, and element can be of any type that may be present in the array.
def func_1(array, element):
    try:
        index = array.index(element)
        return True, index
        #The program returns True indicating that 'element' is found in the 'array', along with its corresponding 'index' position in the array.
    except (ValueError):
        return False, -1
        #The program returns False and -1
    #State of the program after the try-except block has been executed: `array` is a list of elements, and `element` can be of any type. If the `element` is found, the function returns True and the index of the element; otherwise, it returns False and -1.
#Overall this is what the function does:The function accepts a list `array` and an `element` of any type, and attempts to find the index of the element within the array. If the element is found, it returns True and the index of the element; if the element is not found, it returns False and -1. It does not handle cases where the array is empty, but the logic remains consistent in the current implementation.

