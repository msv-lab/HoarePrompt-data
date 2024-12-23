#State of the program right berfore the function call: arr is a list of elements, and element is the element being searched for in the list.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements, `element` is the element being searched for in the list, `index` is either -1 (if the element is not found) or the index of the element in the list (if the element is found), and the function returns `True` and `index` if the element is found, otherwise it returns `False` and `index` is -1.
    return False, -1
    #The program returns False and index -1
#Overall this is what the function does:The function `func_1` accepts two parameters: `arr`, which is a list of elements, and `element`, which is the element being searched for in the list. It iterates through the list to find the specified element. If the element is found, it returns `True` and the index of the element in the list. If the element is not found, it returns `False` and `-1`.

