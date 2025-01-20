#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    sum_n = n * (n + 1) // 2

sum_cubes_n = sum_n ** 2
    return sum_cubes_n - sum_n
    #The program returns (n * (n + 1) // 2) - (n * (n + 1) // 2), which simplifies to 0, since both `sum_cubes_n` and `sum_n` are equal to `n * (n + 1) // 2`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns the value `(n * (n + 1) // 2)

