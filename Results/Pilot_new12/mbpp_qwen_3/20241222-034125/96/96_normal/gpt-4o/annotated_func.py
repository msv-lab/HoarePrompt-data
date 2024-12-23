#State of the program right berfore the function call: tup is a tuple containing elements of any type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: tup is a tuple containing elements of any type, and tup is not empty
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a non-empty tuple, every element in `tup` is of type `first_type`
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a tuple `tup` and checks if all elements in the tuple are of the same type as the first element. If the tuple is empty, it returns `True`. If at least one element in the tuple is of a different type than the first element, it returns `False`. Otherwise, it returns `True`. The function considers the following cases:
- Case_1: If the tuple is empty, the function returns `True`.
- Case_2: If the tuple contains elements of different types, the function returns `False`.
- Case_3: If the tuple contains elements of the same type, the function returns `True`.

The final state of the program after the function concludes will be:
- If the tuple is empty, the function returns `True`.
- If the tuple contains elements of different types, the function returns `False`.
- If the tuple contains elements of the same type, the function returns `True`.

