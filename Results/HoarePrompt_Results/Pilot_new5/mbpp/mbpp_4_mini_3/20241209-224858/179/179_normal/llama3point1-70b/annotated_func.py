#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    return sum(i ** 3 for i in range(2, n * 2 + 1, 2))
    #The program returns the sum of the cubes of all even integers from 2 to n * 2, inclusive
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the sum of the cubes of all even integers from 2 to `n * 2`, inclusive. If `n` is 0, the function returns 0, as there are no even integers in the range.

