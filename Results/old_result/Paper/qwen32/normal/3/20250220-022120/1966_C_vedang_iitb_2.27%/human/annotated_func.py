#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, where each integer is in the range 1 ≤ a_i ≤ 10^9.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: `a_new` is a sorted list of unique integers from `a` where each element from the second to the last element is the difference between the original element and the previous element in the list. `a` remains unchanged. `a_temp` remains a copy of the initial `a_new`. `i` is `len(a_new) - 1`.
    return a_new
    #The program returns `a_new`, which is a sorted list of unique integers from `a` where each element from the second to the last element is the difference between the original element and the previous element in the list.
#Overall this is what the function does:The function accepts a list of integers `a` representing the number of stones in each pile. It returns a sorted list of unique integers where the first element is the smallest unique number from `a`, and each subsequent element is the difference between the current and previous unique, sorted numbers from `a`.

#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, and n is an integer representing the number of piles such that n == len(a) and n >= 1.
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
#Overall this is what the function does:The function `func_2` determines and returns a value of either 1 or 2 based on the configuration of stones in the piles represented by the list `a` and the number of piles `n`. The return value indicates a result of a game or decision-making process involving the piles of stones.

