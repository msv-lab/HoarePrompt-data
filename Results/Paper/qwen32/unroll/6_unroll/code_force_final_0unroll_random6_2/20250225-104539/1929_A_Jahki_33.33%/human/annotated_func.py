#State of the program right berfore the function call: a is a list of integers with length n (2 ≤ n ≤ 100) where each element a_i satisfies 1 ≤ a_i ≤ 10^9, and num2 is an integer representing the length of the list a (i.e., num2 == n).
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` is a list of integers with length `n` (2 ≤ `n` ≤ 100) where each element `a_i` satisfies 1 ≤ `a_i` ≤ 10^9, `num2` is an integer representing the length of the list `a` (i.e., `num2` == `n`), and `order` is the count of non-increasing consecutive pairs in the list `a`.
    if (order == 0) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` checks if the list `a` of integers is strictly increasing. It returns `True` if the list is strictly increasing, and `False` otherwise.

