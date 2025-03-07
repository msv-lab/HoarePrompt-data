#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, where each integer is in the range 1 to 10^9.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: - `a` remains unchanged.
    #- `a_new` becomes a list where the first element is the smallest unique number from the original list, and each subsequent element is the difference between consecutive unique numbers.
    #- `a_temp` remains unchanged as a copy of the original `a_new`.
    #
    #Output State:
    return a_new
    #The program returns `a_new`, which is a list where the first element is the smallest unique number from the original list `a`, and each subsequent element is the difference between consecutive unique numbers.
#Overall this is what the function does:The function takes a list of integers `a` as input, representing the number of stones in each pile, and returns a new list `a_new`. The first element of `a_new` is the smallest unique number from the original list, and each subsequent element is the difference between consecutive unique numbers in ascending order.

#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, and n is a non-negative integer such that 0 <= n <= len(a).
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
#Overall this is what the function does:The function `func_2` determines the outcome of a game based on the number of stones in each pile represented by the list `a` and the integer `n`. It returns 1 if the current player can force a win, and 2 if the opponent can force a win, considering the rules defined by the cases within the function.

