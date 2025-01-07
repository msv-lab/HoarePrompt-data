#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
        
    #State of the program after the  for loop has been executed: If the loop executes, it will return the index of the first tuple found in the tuple `tup`. If no tuple is found, it will return None. `tup` remains unchanged.
    return len(tup)
    #The program returns the length of the tuple `tup`
#Overall this is what the function does:The function `func_1` accepts a tuple `tup` as a parameter. It iterates through the elements of the tuple and if it encounters a tuple element, it returns the index of that tuple element within the tuple `tup`. If no tuple is found, it returns the length of the tuple `tup`. However, the annotations mention cases such as returning the index of a specific element or the second occurrence of an element, which are not implemented in the actual code. Therefore, the actual functionality of the function is to return the index of the first tuple element found in the tuple `tup` or return the length of the tuple if no tuple element is present.

