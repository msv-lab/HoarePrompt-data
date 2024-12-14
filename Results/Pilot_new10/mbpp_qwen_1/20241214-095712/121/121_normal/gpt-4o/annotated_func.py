#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    if (n == 0 or n == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: n is a positive integer and n is neither 0 nor 1
    S0, S1 = 1, 1
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        
        S0, S1 = S1, S_next
        
    #State of the program after the  for loop has been executed: `n` is a positive integer and is greater than 1, `S0` is the nth term in the sequence defined by \(S_0 = 1\), \(S_1 = 1\), and \(S_{i} = 2S_{i-1} + S_{i-2}\) for \(i \geq 2\), `S1` is the (n+1)th term in the same sequence, `i` is `n`.
    return S1
    #The program returns the (n+1)th term in the sequence defined by S0 = 1, S1 = 1, and Si = 2Si-1 + Si-2 for i ≥ 2
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and returns 1 if `n` is either 0 or 1, or the (n+1)th term in the sequence defined by \(S_0 = 1\), \(S_1 = 1\), and \(S_i = 2S_{i-1} + S_{i-2}\) for \(i \geq 2\) if `n` is greater than 1.

