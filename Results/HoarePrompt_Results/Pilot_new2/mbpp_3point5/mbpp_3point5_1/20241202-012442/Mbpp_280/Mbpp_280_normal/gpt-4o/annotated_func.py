#State of the program right berfore the function call: arr is a list of elements and element is any data type.**
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: If the element is found in the list, the function will return True and the index of the element. If the element is not found in the list, the function will return None.
    return False, -1
    #The program returns False, -1
#Overall this is what the function does:The function `func_1` accepts a list `arr` of elements and an `element` of any data type. It iterates through the list to find the `element`. If the `element` is found at index i, it returns True along with the index i. If the `element` is not found, it returns False and index -1.

