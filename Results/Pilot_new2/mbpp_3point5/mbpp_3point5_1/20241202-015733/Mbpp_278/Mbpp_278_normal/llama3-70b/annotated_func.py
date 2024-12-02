#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
        
    #State of the program after the  for loop has been executed: `tup` is a tuple with at least 1 element. The element `elem` is not a tuple. The function returns the index of the first tuple in `tup`, if any. Otherwise, the function returns None.
    return len(tup)
    #The program returns the length of tuple `tup`
#Overall this is what the function does:The function `func_1` accepts a parameter `tup`, which is a tuple. It iterates through the elements of the tuple and checks if an element is a tuple. If it finds a tuple element, it returns the index of that element in the tuple. If no tuple element is found, it returns the length of the tuple. Therefore, the function provides the index of the first tuple element in the tuple if present, otherwise returns the length of the tuple.

