#State of the program right berfore the function call: tup is a tuple.**
def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        
        count += 1
        
    #State of the program after the  for loop has been executed: `tup` is a tuple, `elem` is the first element in the tuple that is not an instance of a tuple, `count` is the number of elements in the tuple before the first tuple is encountered or the loop breaks due to the condition in the if statement.
    return count
    #The program returns the number of elements in the tuple before the first tuple is encountered or the loop breaks due to the condition in the if statement
#Overall this is what the function does:The function func_1 accepts a parameter `tup`, which is a tuple, and iterates through the elements of the tuple. It counts the number of elements in the tuple before encountering the first tuple or breaking the loop due to a condition in the if statement. The function then returns this count. If the tuple has no tuples inside, it will return the total number of elements in the tuple.

