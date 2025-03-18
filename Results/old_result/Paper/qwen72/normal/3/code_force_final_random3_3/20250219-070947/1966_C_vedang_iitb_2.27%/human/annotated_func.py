#State of the program right berfore the function call: a is a list of positive integers (1 <= a_i <= 10^9).
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a` is a list of positive integers (1 <= a_i <= 10^9); `a_new` is a sorted list containing the unique elements of `a`, with each element (starting from index 1) updated to the difference between the original element and the element at the previous index in `a_temp`; `a_temp` is a sorted list containing the unique elements of `a`; `i` is `len(a_new) - 1`, and `len(a_new)` must be greater than 1.
    return a_new
    #The program returns a sorted list `a_new` containing the unique elements of the original list `a`, where each element (starting from index 1) is updated to the difference between the original element and the element at the previous index in `a_temp`. The length of `a_new` is greater than 1.
#Overall this is what the function does:The function `func_1` accepts a list `a` of positive integers and returns a sorted list `a_new` of unique elements from `a`. Each element in `a_new` starting from index 1 is the difference between the current element and the previous element in the sorted list of unique elements. If the length of `a_new` is 1, the function returns a list with a single element, which is the unique element from `a`.

#State of the program right berfore the function call: a is a list of positive integers, and n is a positive integer such that 1 <= n <= len(a).
def func_2(a, n):
    if (n == 1) :
        return 1
        #The program returns 1.
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
#Overall this is what the function does:The function `func_2` accepts a list of positive integers `a` and a positive integer `n` (where 1 <= n <= len(a)). It returns either 1 or 2 based on the following conditions: If `n` is 1, it always returns 1. If `n` is 2, it returns 1 if the first element of `a` is even, otherwise it returns 2. For `n` greater than 2, it recursively checks the rest of the list (`a[1:]`) with `n-1` and returns 1 if the recursive call returns 2 or if it returns 1 and the first element of `a` is not 1; otherwise, it returns 2.

