#State of the program right berfore the function call: a is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9, num2 is an integer such that 1 <= num2 <= 500 representing the number of test cases.
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9, `num2` is an integer such that 1 <= num2 <= 500, `i` is `num2 - 1`, and `order` is the count of indices `j` (0 <= j < num2 - 1) where `a[j]` is greater than or equal to `a[j + 1]`.
    if (order == 0) :
        return True
        #The program returns True.
    else :
        return False
        #The program returns False.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers (where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9) and an integer `num2` (where 1 <= num2 <= 500). It returns `True` if the elements in the list `a` are strictly increasing up to the index `num2 - 1`. Otherwise, it returns `False`.

