#State of the program right berfore the function call: a is a list of positive integers (1 <= a_i <= 10^9).
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a_new` is a list where each element at index `i` (for `i > 0`) is the difference between the element at index `i` and the element at index `i-1` in the sorted list of unique elements of `a`. The first element of `a_new` remains unchanged. `a_temp` remains a sorted list containing the unique elements of `a`.
    return a_new
    #The program returns the list `a_new` where the first element is unchanged, and each subsequent element at index `i` (for `i > 0`) is the difference between the element at index `i` and the element at index `i-1` in the sorted list of unique elements of `a`.
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `a` and returns a new list `a_new`. The first element of `a_new` is the smallest unique element from `a`, and each subsequent element at index `i` (for `i > 0`) is the difference between the element at index `i` and the element at index `i-1` in the sorted list of unique elements of `a`. The original list `a` remains unchanged.

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
                #The program returns the integer 2.
        else :
            winNext = func_2(a[1:], n - 1)
            if (winNext == 2 or winNext == 1 and a[0] != 1) :
                return 1
                #The program returns 1.
            else :
                return 2
                #The program returns the integer 2.
#Overall this is what the function does:The function `func_2` accepts a list of positive integers `a` and a positive integer `n` where 1 <= len(a) <= 2 * 10^5 and 1 <= n <= len(a). It returns either 1 or 2 based on the following conditions: If `n` is 1, it returns 1. If `n` is 2, it returns 1 if the first element of `a` is even, otherwise it returns 2. For `n` greater than 2, it recursively calls itself with the list `a` excluding the first element and `n` decremented by 1. If the result of the recursive call is 2, or if the result is 1 and the first element of `a` is not 1, it returns 1. Otherwise, it returns 2.

