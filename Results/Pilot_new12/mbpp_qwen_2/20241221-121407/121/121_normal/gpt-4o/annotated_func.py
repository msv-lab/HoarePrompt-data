#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: n is a positive integer, and n is neither 0 nor 1
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is at least 2, `S0` is the value of `S1` after the last iteration, `S1` is the value of `S_next` after the last iteration, which is calculated as `2 * S1 + S0` for each iteration.
    return S1
    #The program returns S1 that is calculated as 2 * S1 + S0 for each iteration, starting with i = n and n being at least 2
#Overall this is what the function does:- The annotation suggests that the state of the program after the for loop includes `i` being `n`, which is correct. However, the postcondition regarding the return value of `S1` is accurate, but it does not explicitly mention the initial values of `S0` and `S1` being set to 1, which is crucial for the calculation.

