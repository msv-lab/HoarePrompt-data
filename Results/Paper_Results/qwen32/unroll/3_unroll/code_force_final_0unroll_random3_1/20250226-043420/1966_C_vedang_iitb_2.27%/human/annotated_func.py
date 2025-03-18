#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, where each integer is in the range 1 ≤ a_i ≤ 10^9.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a_new` is a list where the first element is the smallest unique integer from `a`, and each subsequent element is the difference between consecutive elements in the sorted list of unique integers from `a`.
    return a_new
    #The program returns a_new, which is a list where the first element is the smallest unique integer from the list 'a', and each subsequent element is the difference between consecutive elements in the sorted list of unique integers from 'a'.
#Overall this is what the function does:The function takes a list of integers `a` representing the number of stones in each pile and returns a new list where the first element is the smallest unique integer from `a`, and each subsequent element is the difference between consecutive elements in the sorted list of unique integers from `a`.

#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, and n is a positive integer representing the number of piles such that n == len(a).
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
                #The program returns 2.
        else :
            winNext = func_2(a[1:], n - 1)
            if (winNext == 2 or winNext == 1 and a[0] != 1) :
                return 1
                #The program returns 1.
            else :
                return 2
                #The program returns 2
#Overall this is what the function does:The function `func_2` determines a winning strategy for a game involving piles of stones. It accepts a list `a` of integers representing the number of stones in each pile and a positive integer `n` representing the number of piles such that `n == len(a)`. The function returns 1 if the current player can force a win, and 2 if the opponent can force a win, based on the configuration of the piles.

