#State of the program right berfore the function call: tup is a tuple containing elements of any data type.
def func_1(tup):
    if (not tup) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`tup` is a tuple containing elements of any data type, and `tup` is not empty.
    first_type = type(tup[0])
    for element in tup:
        if type(element) != first_type:
            return False
        
    #State of the program after the  for loop has been executed: `tup` is a tuple containing elements of the same data type, `first_type` is the type of the first element in `tup`, and all elements in `tup` are of type `first_type`.
    return True
    #The program returns True, indicating that all elements in the tuple 'tup' are of the same data type, which is 'first_type'.
#Overall this is what the function does:The function accepts a tuple `tup` and checks whether the tuple is empty. If it is empty, it returns True. If not, it verifies if all elements in the tuple are of the same data type. If all elements are of the same data type, it returns True; otherwise, it returns False. However, the function fails to account for the specific case where the first element is a boolean, which is treated as a distinct type, potentially causing unexpected returns. Therefore, it can also return False if any element is of an unexpected type while checking for type consistency.

