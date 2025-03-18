#State of the program right berfore the function call: a is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9, num2 is an integer representing the number of test cases where 1 <= num2 <= 500.
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` remains unchanged, `num2` remains unchanged, `order` is the number of times an element in the list `a` is not greater than the next element in the list, for the first `num2 - 1` elements.
    if (order == 0) :
        return True
        #The program returns True.
    else :
        return False
        #The program returns False.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `num2`. It returns `True` if the first `num2 - 1` elements of the list `a` are in strictly increasing order, and `False` otherwise. The function does not modify the input list `a` or the integer `num2`.

