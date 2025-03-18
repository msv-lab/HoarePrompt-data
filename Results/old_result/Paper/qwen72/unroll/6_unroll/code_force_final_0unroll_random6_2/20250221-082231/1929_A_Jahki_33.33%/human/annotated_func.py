#State of the program right berfore the function call: a is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9, num2 is an integer representing the number of test cases where 1 <= num2 <= 500.
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` remains unchanged, `num2` remains unchanged, `order` is the number of times an element in the list `a` is greater than or equal to the next element in the list.
    if (order == 0) :
        return True
        #The program returns True.
    else :
        return False
        #The program returns False.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers (with a length between 2 and 100, and each integer between 1 and 10^9) and an integer `num2` (representing the number of test cases, between 1 and 500). It returns `True` if the list `a` is strictly increasing (i.e., no element is greater than or equal to the next element). Otherwise, it returns `False`. The function does not modify the input list `a` or the integer `num2`.

