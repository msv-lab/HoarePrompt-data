#State of the program right berfore the function call: **arr is a list of elements and element is any data type.**
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: After the loop executes, `arr` is a list with elements, `index` is the index of the first occurrence of `element` in the list, and `value` is the element that is equal to `element`. If no element is equal to `element`, the program does not return anything.
    return False, -1
    #The program returns False and -1 if no element is equal to `element` in the list `arr`.
#Overall this is what the function does:Functionality: The function `func_1` accepts two parameters: a list `arr` consisting of elements of any data type and an `element` of any data type. It iterates through the list and if it finds the `element`, it returns True along with the index of the first occurrence of the `element` in the list. If the `element` is not found, the function returns False along with -1. The function does not return the value of the index as stated in the annotations for any case.

