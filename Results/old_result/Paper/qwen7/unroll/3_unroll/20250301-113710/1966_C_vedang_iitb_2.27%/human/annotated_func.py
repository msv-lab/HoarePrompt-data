#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and a_new is a list that will store the modified values after applying the function.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: `a` is a list where each element at index i (starting from 1) is the difference between the corresponding element in `a_new` and the element at index (i-1) in `a_temp`. `a_temp` is a copy of `a_new` at the start of the loop, and `a` remains unchanged from its initial state.
    return a_new
    #The program returns a list `a_new` where each element at index i (starting from 1) is the difference between the corresponding element in `a_new` and the element at index (i-1) in `a_temp`. The list `a` remains unchanged from its initial state.
#Overall this is what the function does:The function `func_1` accepts a list `a` of non-negative integers. It first removes duplicates and sorts the list, then calculates the difference between consecutive elements in the sorted list to create a new list `a_new`. Finally, it returns this new list `a_new` while ensuring the original list `a` remains unchanged.

#State of the program right berfore the function call: a is a list of n non-negative integers representing the initial number of stones in each pile, and n is a positive integer such that 1 <= n <= 2 * 10^5.
def func_2(a, n):
    if (n == 1) :
        return 1
        #The program returns 1
    else :
        if (n == 2) :
            if (a[0] % 2 == 0) :
                return 1
                #The program returns 1
            else :
                return 2
                #The program returns 2
        else :
            winNext = func_2(a[1:], n - 1)
            if (winNext == 2 or winNext == 1 and a[0] != 1) :
                return 1
                #The program returns 1
            else :
                return 2
                #The program returns 2
#Overall this is what the function does:The function accepts a list `a` of `n` non-negative integers representing the initial number of stones in each pile, and an integer `n` indicating the number of piles (with 1 <= n <= 2 * 10^5). It determines whether the player who starts can guarantee a win based on the current configuration of stone piles. If the starting player can guarantee a win, the function returns 1; otherwise, it returns 2.

