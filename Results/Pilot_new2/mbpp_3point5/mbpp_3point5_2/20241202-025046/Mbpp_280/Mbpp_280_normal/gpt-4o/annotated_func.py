#State of the program right berfore the function call: arr is a list of elements and element is any data type.**
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: If the loop executes, the output will be True and the index of the element in the list 'arr' that matches the given 'element'. If the loop does not execute, the output will be False and -1 as the index value
    return False, -1
    #The program returns False and -1 as the index value
#Overall this is what the function does:The function `func_1` accepts a list `arr` containing elements of any data type and an `element` which can be any data type. It iterates through the elements of the list and if it finds an element that matches the given `element`, it returns True along with the index of that element in the list. If no matching element is found, it returns False along with -1 as the index value. The function accurately handles different cases where the `element` matches elements at different positions in the list.

