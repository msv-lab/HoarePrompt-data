#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: n is a positive integer, and n is neither 0 nor 1, which implies that n is greater than 1
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than 1, `S0` is the second to last term in the sequence, `S1` is the last term in the sequence where each term is calculated as `2 * previous_term + term_before_previous`, `i` is `n + 1`.
    return S1
    #The program returns S1, which is the last term in the sequence calculated as per the given formula, where each term depends on the two preceding terms.
#Overall this is what the function does:The function accepts an integer `n`, returns 1 if `n` is 0 or 1, and for `n > 1`, returns the `n`-th term of a sequence where each term is calculated as `2 * previous_term + term_before_previous`. The function is designed for non-negative integer inputs and may throw errors for negative integers or non-integer inputs due to the nature of the `range` function in Python.

