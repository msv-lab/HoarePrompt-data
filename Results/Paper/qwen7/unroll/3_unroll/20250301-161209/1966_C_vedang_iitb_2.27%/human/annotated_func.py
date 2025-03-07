#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and the length of the list (n) satisfies 1 <= n <= 2 * 10^5.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: `a_temp` is a copy of `a_new`, both `a_temp` and `a_new` are sorted lists of unique elements from the original list `a`, with each element in `a_new` updated to be the difference between itself and the previous element in `a_temp`.
    return a_new
    #`a_new` is a sorted list of unique elements where each element is the difference between the corresponding element in the original `a_temp` list and the previous element in `a_temp`.
#Overall this is what the function does:The function accepts a list of non-negative integers `a` and returns a new sorted list `a_new` containing unique elements. Each element in `a_new` represents the difference between the corresponding element in a temporary sorted and unique list `a_temp` and the previous element in `a_temp`.

#State of the program right berfore the function call: a is a list of n non-negative integers representing the number of stones in each of the n piles, and n is a positive integer such that 1 <= n <= 2 * 10^5.
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
#Overall this is what the function does:The function accepts a list `a` of `n` non-negative integers and an integer `n`. It determines whether the first player has a winning strategy based on the initial configuration of stone piles. If the first player can guarantee a win, the function returns 1; otherwise, it returns 2.

