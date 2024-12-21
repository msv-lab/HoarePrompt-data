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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 1, `S0` is the value from position `n-1` in the sequence, `S1` is the value from position `n` in the sequence.
    return S1
    #The program returns the value from position `n` in the sequence, which is represented by `S1`
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is 0 or 1, it returns 1. For any integer `n` greater than 1, it computes the value at position `n` in a specific sequence defined by the recurrence relation `S_next = 2 * S1 + S0`, where `S0` and `S1` are initialized to 1. The function ultimately returns this computed value at position `n`, which is represented by `S1`. Notably, there is no handling for negative integers, and the function does not validate input types, meaning it may raise an error if a non-integer is passed.

