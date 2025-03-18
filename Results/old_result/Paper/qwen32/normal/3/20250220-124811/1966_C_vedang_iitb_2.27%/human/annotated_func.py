#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, where each integer is in the range 1 to 10^9.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a` is a list of integers representing the number of stones in each pile, where each integer is in the range 1 to 10^9; `a_new` is a sorted list of unique integers from `a` where each element (except the first) is the difference between its original value and the previous element in the sorted list; `a_temp` is a copy of `a_new`.
    return a_new
    #The program returns `a_new`, which is a sorted list of unique integers from the original list `a`, where each element (except the first) is the difference between its original value and the previous element in the sorted list.
#Overall this is what the function does:The function accepts a list of integers representing the number of stones in each pile and returns a sorted list of unique integers. Each element in the returned list (except the first) is the difference between its value and the previous element in the sorted list.

#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, and n is a non-negative integer such that 1 <= n <= len(a).
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
                #The program returns 1.
            else :
                return 2
                #The program returns 2
#Overall this is what the function does:The function `func_2` determines whether the first player can win a game given a list of piles of stones and a number of piles to consider, returning 1 if the first player can win and 2 if the second player can win.

