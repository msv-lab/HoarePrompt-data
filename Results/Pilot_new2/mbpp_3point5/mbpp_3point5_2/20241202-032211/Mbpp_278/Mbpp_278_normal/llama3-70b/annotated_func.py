#State of the program right berfore the function call: tup is a tuple.**
def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
        
    #State of the program after the  for loop has been executed: At the end of the loop, `tup` remains unchanged, and the loop will terminate after checking all elements of `tup`. The function will return the index of the first tuple found in `tup`, if one exists. Otherwise, it will return None.
    return len(tup)
    #The program returns the length of the tuple `tup`
#Overall this is what the function does:The function func_1 accepts a parameter `tup`, which is a tuple. It iterates through the elements of the tuple and returns the index of the first tuple found in `tup`. If no tuple is found, the function returns the length of the tuple `tup`.

