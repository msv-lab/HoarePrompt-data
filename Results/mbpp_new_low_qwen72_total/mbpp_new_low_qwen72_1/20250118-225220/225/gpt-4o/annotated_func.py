#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    sum_n = n * (n + 1) // 2

sum_cubes_n = sum_n ** 2
    return sum_cubes_n - sum_n
    #The program returns the value of `sum_cubes_n - sum_n`, where `sum_cubes_n` is `(n * (n + 1) // 2)` and `sum_n` is `n * (n + 1) // 2`. Since both `sum_cubes_n` and `sum_n` are the same, the program returns 0.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns the value of `sum_cubes_n - sum_n`, where `sum_cubes_n` is the square of the sum of the first `n` natural numbers (`(n * (n + 1) // 2)

