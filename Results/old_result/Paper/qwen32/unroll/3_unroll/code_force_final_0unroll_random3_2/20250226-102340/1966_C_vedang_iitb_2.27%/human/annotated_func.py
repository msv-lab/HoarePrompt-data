#State of the program right berfore the function call: a is a list of positive integers representing the number of stones in each pile.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: a_new = [1, 1, 1, 1]
    return a_new
    #The program returns the list [1, 1, 1, 1]
#Overall this is what the function does:The function accepts a list of positive integers representing the number of stones in each pile and returns a list of ones with a length that depends on the number of unique, sorted values in the input list.

#State of the program right berfore the function call: a is a list of integers representing the number of stones in each pile, and n is a non-negative integer representing the number of piles such that 1 <= n <= len(a).
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
#Overall this is what the function does:The function `func_2` determines the winner of a game based on the number of stones in each pile and the number of piles. It returns `1` if the first player wins and `2` if the second player wins, considering various cases based on the number of piles and the parity of stones in the first pile.

