#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
        
    #State of the program after the  for loop has been executed: `tup` is a tuple. The loop will iterate through each element in the tuple. If the element is a tuple, the function will return the index of that element in the original tuple `tup`. If no tuple elements are found, the function will return None.
    return len(tup)
    #The program returns the length of the tuple `tup`
#Overall this is what the function does:The function `func_1` accepts a parameter `tup`, which is a tuple. It iterates through each element in the tuple and if an element is a tuple, it returns the index of that element in the original tuple `tup`. If no tuple elements are found, the function returns the length of the tuple `tup`.

