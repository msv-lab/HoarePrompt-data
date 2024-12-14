#State of the program right berfore the function call: x and y are positive integers.
def func_1(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor (GCD) of the original values of `x` and `y` (the initial values), `y` must have been greater than 0 for the loop to execute.
    return x
    #The program returns the greatest common divisor (GCD) of the original values of 'x' and 'y', where 'y' was greater than 0 for the loop to execute
#Overall this is what the function does:The function accepts two positive integers `x` and `y`, and returns the greatest common divisor (GCD) of `x` and `y`. If `y` is 0 at the start, the function will directly return `x` as the GCD, since the GCD of any number and 0 is the number itself.

#State of the program right berfore the function call: m is a positive integer such that 1 <= m <= 10^9, a and b are positive integers such that 1 <= a, b <= 10^5.
def func_2(m, a, b):
    g = func_1(a, b)
    if (g != 1) :
        return func_2(m // g, a // g, b // g) * g
        #The program returns the result of func_2 with parameters (m // g, a // g, b // g) multiplied by g, where g is the result of func_1(a, b) and is not equal to 1.
    #State of the program after the if block has been executed: *`m` is a positive integer such that 1 <= m <= 10^9; `a` is a positive integer such that 1 <= a <= 10^5; `b` is a positive integer such that 1 <= b <= 10^5; `g` is equal to 1, which is the result of `func_1(a, b)`
    k = a + b - 1
    if (m < k) :
        return (m + 1) * (m + 2) // 2
        #The program returns the result of the formula (m + 1) * (m + 2) // 2, where 'm' is a positive integer less than 'k', and 'k' is equal to a + b - 1
    #State of the program after the if block has been executed: *`m` is a positive integer such that 1 <= m <= 10^9; `a` is a positive integer such that 1 <= a <= 10^5; `b` is a positive integer such that 1 <= b <= 10^5; `g` is equal to 1, which is the result of `func_1(a, b)`; `k` is equal to `a + b - 1`; `m` is greater than or equal to `k`.
    sum_k = k * (k + 1) // 2
    sum_m = m * (m + 1) // 2 - k * (k - 1) // 2
    return sum_k + sum_m
    #The program returns the sum of `sum_k`, which is equal to `(a + b - 1) * (a + b) // 2`, and `sum_m`, which is equal to `m * (m + 1) // 2 - k * (k - 1) // 2`
#Overall this is what the function does:The function accepts three parameters: positive integers `m`, `a`, and `b`. It first calls another function `func_1(a, b)` to obtain `g`. If `g` is not equal to 1, it recursively calls itself with modified parameters `(m // g, a // g, b // g)`, multiplying the result by `g`. If `m` is less than `k` (where `k` is `a + b - 1`), it returns the sum of the first `m + 1` integers. If neither of these conditions hold, it calculates and returns the sum of two series: one up to `k` and another from `k` to `m`. The function can therefore handle different scenarios based on the values of `g`, `m`, `a`, and `b` while involving multiple recursive calls if `g` is greater than 1.

