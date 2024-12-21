#State of the program right berfore the function call: lst is a list and element is any type of object that can be compared with the elements of lst.
def func_1(lst, element):
    for item in lst:
        if item != element:
            return False
        
    #State of the program after the  for loop has been executed: `lst` is a list where either all elements are equal to `element` if the list is not empty, or `lst` is empty (in which case the condition is considered true by default due to the lack of elements to compare), and `element` remains unchanged. If the loop completes without returning `False`, it implies all elements in `lst` are equal to `element`.
    return True
    #The program returns True, indicating that all elements in the list `lst` are equal to `element` if the list is not empty, or the list `lst` is empty
#Overall this is what the function does:The function checks if all elements in a given list (`lst`) are equal to a specified `element`. If the list is empty, it returns `True` by default. For non-empty lists, it returns `True` if all elements match the specified `element` and `False` otherwise. The function leaves the input `lst` and `element` unchanged. It handles lists of any size (including empty lists) and elements of any comparable type. The function performs a linear search through the list, comparing each element to the specified `element`, and returns as soon as it finds a mismatch or completes the comparison without finding any mismatches.

