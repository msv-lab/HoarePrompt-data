#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n < 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n is a non-negative integer, and n is greater than or equal to 0
    perrin = [3, 0, 2]
    for i in range(3, n + 1):
        perrin.append(perrin[i - 2] + perrin[i - 3])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than or equal to 3, `perrin` is a list of length `n + 1` where the elements are `[3, 0, 2, perrin[3], perrin[4], ..., perrin[n]]` and each `perrin[i]` for `i >= 3` is `perrin[i - 2] + perrin[i - 3]`
    return sum(perrin)
    #The program returns the sum of the Perrin sequence up to the nth term, where `n` is a non-negative integer greater than or equal to 3, and the sequence starts with [3, 0, 2]. Each subsequent term is the sum of the terms two places and three places back in the sequence.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns the sum of the Perrin sequence up to the nth term. The Perrin sequence starts with the initial values [3, 0, 2], and each subsequent term is the sum of the terms two places and three places back in the sequence. If `n` is less than 0, the function returns 0. If `n` is 0, 1, or 2, the function returns the sum of the initial segment of the Perrin sequence up to the nth term, which is 3, 3, or 5 respectively. For `n` greater than or equal to 3, the function computes the full Perrin sequence up to the nth term and returns the sum of all terms in the sequence.

