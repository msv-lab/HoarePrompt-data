#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer, and `n` is greater than 1.
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 1, `S0` is the value of `S1` from the last iteration, `S1` is the value of `S_next` from the last iteration, `i` is `n + 1`.
    return S1
    #The program returns the value of S1 from the last iteration, which is derived from the previous calculations involving S0 and S_next, where n is a non-negative integer greater than 1, and i is n + 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 1 if `n` is 0 or 1. If `n` is greater than 1, it calculates and returns the value of `S1` from the last iteration of a loop where `S0` and `S1` are updated based on the previous values. The calculation involves the recurrence relation `S_next = 2 * S1 + S0`, which generates a sequence based on the input `n`.

