#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. num2 is not used in the problem description and should be ignored.
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 500; `n` is an integer such that 2 ≤ n ≤ 100; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 10^9; `order` is the count of times `a[i - 1] >= a[i]` is true for `i` from 1 to `n - 1`.
    if (order == 0) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` takes a list `a` of `n` integers and an unused parameter `num2`. It returns `True` if the list `a` is strictly increasing (i.e., each element is less than the next one), and `False` otherwise.

