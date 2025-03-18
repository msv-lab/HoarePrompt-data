#State of the program right berfore the function call: tup is a tuple.**
def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
        
    #State of the program after the  for loop has been executed: `tup` is a tuple, `elem` is an instance of tuple and present in `tup`. The function returns the index of the first tuple found in `tup`. If no tuple is found in `tup`, the function returns None.
    return len(tup)
    #The program returns the length of the tuple `tup`
#Overall this is what the function does:The function `func_1` accepts a parameter `tup`, which is a tuple. It iterates through the elements of the tuple and returns the index of the first tuple found in `tup`. If no tuple is found, it returns the length of the tuple `tup`.

