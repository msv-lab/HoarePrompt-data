#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and a is not empty.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: `a_new` is a list where each element (starting from the second) is reduced by the corresponding element in `a_temp` up to the previous index. `a` and `a_temp` remain unchanged.
    return a_new
    #`a_new` is a list where each element (starting from the second) is reduced by the corresponding element in `a_temp` up to the previous index. `a` and `a_temp` remain unchanged. The function returns `a_new`.
#Overall this is what the function does:The function accepts a list of non-negative integers `a`, representing the initial number of stones in each pile. It returns a new list `a_new` where each element (starting from the second) is reduced by the corresponding element in a temporary copy of the sorted and unique version of `a` up to the previous index. The original list `a` and the temporary list `a_temp` remain unchanged.

#State of the program right berfore the function call: a is a list of n non-negative integers representing the initial number of stones in each of the n piles, and n is a positive integer such that 1 <= n <= 2*10^5.
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
#Overall this is what the function does:The function accepts a list `a` of non-negative integers representing the initial number of stones in each pile, and an integer `n` indicating the number of piles. It recursively determines whether the player who starts the game can guarantee a win based on the current configuration of stone piles. If the starting player can guarantee a win, the function returns 1; otherwise, it returns 2.

