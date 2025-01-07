#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1 regardless of the initial non-negative integer value of n, which is either 0 or 1.
    #State of the program after the if block has been executed: *`n` is a non-negative integer and `n` is greater than 1
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `S0` is the value of `S1` from the last iteration, `S1` is the value computed in the last iteration, `n` is greater than 1.
    return S1
    #The program returns the value of S1, which was computed in the last iteration.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 1 if `n` is 0 or 1; otherwise, it calculates and returns the last value of a sequence based on `n` using a defined recurrence relation.

