#State of the program right berfore the function call: arr is a list and element is any data type that can be compared with the elements in arr.**
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: If the loop executes, it means that the element was found in arr at some index. Therefore, after all iterations of the loop, the output state would be `arr` is a list with at least one element, `index` is the index where element was found, `value` is the element equal to `element`. If the loop does not execute, the output state would be `arr` is a list, `index` is not defined, `value` is not defined.
    return False, -1
    #If the loop does not execute, the program returns False, -1 as `arr` is a list, `index` is not defined, and `value` is not defined.
#Overall this is what the function does:The function `func_1` accepts a list `arr` and an element `element`. It iterates through the list `arr` and returns True along with the index where the `element` is found if it exists in the list. If the `element` is not found, it returns False and -1 as the index value. The function accurately handles the cases where the element is found, the element is not found, and also when the loop does not execute.

