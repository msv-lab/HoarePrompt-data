#State of the program right berfore the function call: tup is a tuple.
def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        
        count += 1
        
    #State of the program after the  for loop has been executed: `tup` is a tuple with at least 1 element, `elem` is the last element in the tuple, `count` is the number of elements in the tuple before the first tuple element is encountered or the total number of elements if no tuple is encountered
    return count
    #The program returns the number of elements in the tuple before the first tuple element is encountered or the total number of elements if no tuple is encountered
#Overall this is what the function does:The function func_1 accepts a tuple `tup` as a parameter. It iterates through the elements of the tuple until it encounters the first tuple element. It then returns the number of elements in the tuple before the first tuple element is encountered or the total number of elements if no tuple is encountered. If the tuple is empty, it returns 0.

