#State of the program right berfore the function call: a is a list of positive integers (1 <= a_i <= 10^9) representing the initial number of stones in each pile.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a_new` is a sorted list containing the unique elements from `a`, and for each element `a_new[i]` (where 1 <= i < len(a_new)), `a_new[i]` is now `a_new[i] - a_temp[i - 1]`. The length of `a_new` and `a_temp` remains unchanged.
    return a_new
    #The program returns a sorted list `a_new` where each element `a_new[i]` (for 1 <= i < len(a_new)) has been modified to `a_new[i] - a_temp[i - 1]`. The length of `a_new` remains the same as the length of `a_temp`.
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers and returns a sorted list `a_new` containing the unique elements from `a`. Each element `a_new[i]` (for 1 <= i < len(a_new)) is modified to be the difference between `a_new[i]` and the previous element in the original sorted unique list `a_temp[i - 1]`. The length of `a_new` is the same as the number of unique elements in `a`.

#State of the program right berfore the function call: a is a list of positive integers where 1 <= len(a) <= 2 * 10^5, and n is a positive integer such that 1 <= n <= len(a).
def func_2(a, n):
    if (n == 1) :
        return 1
        #The program returns the integer 1.
    else :
        if (n == 2) :
            if (a[0] % 2 == 0) :
                return 1
                #The program returns 1.
            else :
                return 2
                #The program returns 2.
        else :
            winNext = func_2(a[1:], n - 1)
            if (winNext == 2 or winNext == 1 and a[0] != 1) :
                return 1
                #The program returns 1.
            else :
                return 2
                #The program returns 2.
#Overall this is what the function does:The function `func_2` accepts a list `a` of positive integers and a positive integer `n` where `1 <= n <= len(a)`. It returns either 1 or 2 based on the following conditions: If `n` is 1, it returns 1. If `n` is 2, it returns 1 if the first element of `a` is even, otherwise it returns 2. For `n` greater than 2, it recursively calls itself with the list `a` excluding the first element and `n` decremented by 1. If the recursive call returns 2, or if it returns 1 and the first element of `a` is not 1, the function returns 1. Otherwise, it returns 2.

