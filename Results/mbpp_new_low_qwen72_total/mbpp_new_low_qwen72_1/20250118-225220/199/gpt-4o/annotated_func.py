#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n < 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n is a non-negative integer, and n is greater than or equal to 0
    perrin = [3, 0, 2]
    for i in range(3, n + 1):
        perrin.append(perrin[i - 2] + perrin[i - 3])
        
    #State of the program after the  for loop has been executed: perrin = [3, 0, 2] + [perrin[i - 2] + perrin[i - 3] for i in range(3, n + 1)]
    return sum(perrin)
    #The program returns the sum of the list `perrin`, which starts with [3, 0, 2] and continues with elements calculated as the sum of the element two positions back and the element three positions back, for each index from 3 to n inclusive. The exact sum depends on the value of `n`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is negative, the function returns 0. Otherwise, it calculates the Perrin sequence up to the `n`-th term, where the sequence starts with [3, 0, 2] and each subsequent term is the sum of the term two positions back and the term three positions back. The function then returns the sum of the entire Perrin sequence up to the `n`-th term. The exact sum depends on the value of `n`.

