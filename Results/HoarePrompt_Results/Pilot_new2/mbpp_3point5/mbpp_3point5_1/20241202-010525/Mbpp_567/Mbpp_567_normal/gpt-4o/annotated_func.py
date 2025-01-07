#State of the program right berfore the function call: lst is a list of comparable elements.**
def func_1(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        
    #State of the program after the  for loop has been executed: After the loop executes, `lst` is a list of comparable elements. If `lst[i]` is ever greater than `lst[i+1]` during the loop, the function will return False.
    return True
    #The program returns True unless at any point during the loop, lst[i] is greater than lst[i+1]
#Overall this is what the function does:The function func_1 accepts a list lst of comparable elements. It iterates through the list and returns False if it encounters an element greater than the next element. Otherwise, it returns True.

