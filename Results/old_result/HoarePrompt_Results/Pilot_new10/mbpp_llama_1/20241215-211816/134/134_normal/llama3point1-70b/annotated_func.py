#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum += math.comb(n, i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `sum` is `2^(n-1)`
    return sum
    #The program returns 2 raised to the power of (n-1) where n is a positive integer
#Overall this is what the function does:The function accepts a positive integer n and returns the sum of binomial coefficients "n choose i" for all even i from 0 to n

