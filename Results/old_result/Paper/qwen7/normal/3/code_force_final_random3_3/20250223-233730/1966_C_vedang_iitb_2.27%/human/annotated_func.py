#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and the length of the list (n) satisfies 1 <= n <= 2 * 10^5.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: After the loop executes all its iterations, `a_new` will have each of its elements (starting from the second element) updated such that `a_new[i]` is equal to the original value of `a_new[i]` minus the cumulative sum of all previous elements in `a_new` up to `a_new[i-1]`. Specifically, `a_temp` will be a copy of `a_new` where the first element remains unchanged, and `i` will be equal to `len(a_new)`. The length of `a_new` must be at least 1 for the loop to execute.
    #
    #In simpler terms, after the loop completes, each element in `a_new` (except the first one) will be adjusted to reflect the difference between its original value and the sum of all preceding elements in the list.
    return a_new
    #a_new is a list where each element (starting from the second element) is the original value minus the cumulative sum of all previous elements. The first element remains unchanged, and i is the length of a_new.
#Overall this is what the function does:The function accepts a list `a` of non-negative integers and returns a new list `a_new`. In `a_new`, the first element is the same as in `a`, while each subsequent element is calculated as the original value minus the sum of all previous elements in the list `a`.

#State of the program right berfore the function call: a is a list of n integers representing the initial number of stones in each pile, and n is a positive integer such that 1 <= n <= 2 * 10^5.
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
#Overall this is what the function does:The function accepts a list `a` of `n` integers representing the initial number of stones in each pile, and an integer `n` indicating the number of piles. It determines whether the player who starts the game can guarantee a win based on the current configuration of stones. If the starting player can guarantee a win, the function returns 1; otherwise, it returns 2.

