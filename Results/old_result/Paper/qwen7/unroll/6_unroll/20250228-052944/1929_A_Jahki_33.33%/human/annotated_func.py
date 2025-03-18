#State of the program right berfore the function call: a is a list of integers representing the array elements, and num2 is not used in the function and can be ignored.
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: Output State: `a` is a list of integers representing the array elements, and order is the number of adjacent swaps needed to sort the list in non-decreasing order.
    if (order == 0) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function accepts a list of integers `a` and returns `True` if the list is already sorted in non-decreasing order, otherwise it returns `False`.

