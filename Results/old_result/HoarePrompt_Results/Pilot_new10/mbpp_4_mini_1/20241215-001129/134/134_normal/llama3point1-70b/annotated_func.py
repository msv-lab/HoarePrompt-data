#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum += math.comb(n, i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `sum` is equal to the sum of `math.comb(n, i)` for all even `i` from `0` to `n`.
    return sum
    #The program returns the sum of math.comb(n, i) for all even i from 0 to n, where n is a positive integer.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the sum of `math.comb(n, i)` for all even integers `i` from 0 to `n`, where `math.comb(n, i)` calculates the number of combinations of `n` items taken `i` at a time.

