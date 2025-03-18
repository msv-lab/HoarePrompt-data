#State of the program right berfore the function call: a is a list of positive integers (1 <= a_i <= 10^9).
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a_new` is a list where each element (except the first one) is the difference between the original element and the previous element in the sorted unique list `a_temp`. The first element of `a_new` remains unchanged, and `a_temp` remains a sorted list of unique elements from `a`.
    return a_new
    #The program returns the list `a_new`, where the first element is the same as the first element of the sorted unique list `a_temp`, and each subsequent element is the difference between the corresponding element in `a_temp` and the previous element in `a_temp`.
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers and returns a new list `a_new`. The first element of `a_new` is the smallest unique element from `a`, and each subsequent element is the difference between consecutive unique elements from `a` when sorted. The original list `a` remains unchanged.

#State of the program right berfore the function call: a is a list of positive integers where 1 <= len(a) <= 2 * 10^5, and n is a positive integer such that n == len(a).
def func_2(a, n):
    if (n == 1) :
        return 1
        #The program returns the integer 1.
    else :
        if (n == 2) :
            if (a[0] % 2 == 0) :
                return 1
                #The program returns the integer 1.
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
                #The program returns 2.
#Overall this is what the function does:The function `func_2` accepts a list `a` of positive integers and an integer `n` where `n` is the length of `a`. It returns either the integer 1 or the integer 2 based on the following conditions: If the length of the list `a` is 1, it returns 1. If the length of the list `a` is 2, it returns 1 if the first element of `a` is even, otherwise it returns 2. For lists longer than 2 elements, it recursively checks the sub-list `a[1:]` and returns 1 if the recursive call returns 2 or if it returns 1 and the first element of `a` is not 1; otherwise, it returns 2.

