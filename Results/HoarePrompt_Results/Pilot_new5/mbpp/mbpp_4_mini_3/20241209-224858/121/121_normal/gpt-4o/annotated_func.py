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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 1, `S0` is the value of `S1` from the last iteration, `S1` is the value of `S_next` at `i = n`.
    return S1
    #The program returns S1, which is the value of S_next at i = n
#Overall this is what the function does:The function accepts a non-negative integer `n`. It returns 1 if `n` is 0 or 1. For any `n` greater than 1, it computes a sequence using the formula `S_next = 2 * S1 + S0`, where `S0` and `S1` are initialized to 1. The function ultimately returns the value of `S1`, which represents the computed result for the input `n`.

