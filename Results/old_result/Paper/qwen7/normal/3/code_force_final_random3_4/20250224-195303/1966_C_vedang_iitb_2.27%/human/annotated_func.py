#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and a_new is a list that will store the transformed values after applying the function.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to the length of `a_new` minus 1; every element in `a_new` starting from the second element (`a_new[1]`) will have been reduced by the corresponding element in `a_temp` up to one less than its original index. In other words, for each `i` from 1 to the length of `a_new` minus 1, `a_new[i]` will be `a_new[i] - a_temp[i-1]`.
    #
    #This means that if `a_new` originally had `n` elements, after the loop completes, `a_new[1]` will be `a_new[1] - a_temp[0]`, `a_new[2]` will be `a_new[2] - a_temp[1]`, and so on, until `a_new[n-1]` will be `a_new[n-1] - a_temp[n-2]`.
    return a_new
    #The program returns a_new, where each element starting from the second element (a_new[1]) has been reduced by the corresponding element in a_temp up to one less than its original index.
#Overall this is what the function does:The function accepts a list of non-negative integers `a`. It first removes duplicates and sorts the list. Then, it creates a new list `a_new` where each element starting from the second one is reduced by the corresponding element in a temporary list `a_temp`, which is a copy of the sorted unique list `a_new`. Finally, it returns the transformed list `a_new`.

#State of the program right berfore the function call: a is a list of n integers representing the initial number of stones in each pile, and n is a positive integer such that 1 <= n <= 2*10^5.
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
#Overall this is what the function does:The function accepts a list `a` of `n` integers representing the initial number of stones in each pile, and an integer `n` indicating the number of piles. It recursively determines whether the player who starts can guarantee a win based on the current configuration of stone piles. The function returns 1 if the starting player can win, and 2 otherwise.

