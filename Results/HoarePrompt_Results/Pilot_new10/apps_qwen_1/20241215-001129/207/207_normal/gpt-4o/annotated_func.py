#State of the program right berfore the function call: x and y are non-negative integers, representing the values of \(a\) and \(b\) respectively in the problem description.
def func_1(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the greatest common divisor (GCD) of `x_initial` and `y_initial`; `y` is 0
    return x
    #The program returns x which is the greatest common divisor (GCD) of x_initial and y_initial
#Overall this is what the function does:The function accepts two non-negative integers `x` and `y`, and returns the greatest common divisor (GCD) of these two numbers using the Euclidean algorithm. The algorithm repeatedly replaces `x` with `y` and `y` with `x % y` until `y` becomes 0, at which point `x` contains the GCD of the original `x` and `y`.

#State of the program right berfore the function call: m is a non-negative integer such that \(1 \leq m \leq 10^9\), a and b are positive integers such that \(1 \leq a, b \leq 10^5\).
def func_2(m, a, b):
    g = func_1(a, b)
    if (g != 1) :
        return func_2(m // g, a // g, b // g) * g
        #`The program returns the result of calling `func_2(m // g, a // g, b // g)` and then multiplying it by `g`, where `g` is the return value of `func_1(a, b)` and `m`, `a`, and `b` are as defined in the initial state
    #State of the program after the if block has been executed: `m` is a non-negative integer such that \(1 \leq m \leq 10^9\), `a` is a positive integer such that \(1 \leq a \leq 10^5\), `b` is a positive integer such that \(1 \leq b \leq 10^5\), `g` is the return value of `func_1(a, b)`, and \(g = 1\)
    k = a + b - 1
    if (m < k) :
        return (m + 1) * (m + 2) // 2
        #The program returns (m + 1) * (m + 2) // 2, where m is a non-negative integer such that 1 ≤ m ≤ 10^9 and the current value of m is less than k, and k is a positive integer equal to a + b - 1, with a and b being positive integers such that 1 ≤ a, b ≤ 10^5
    #State of the program after the if block has been executed: `m` is a non-negative integer such that \(1 \leq m \leq 10^9\), `a` is a positive integer such that \(1 \leq a \leq 10^5\), `b` is a positive integer such that \(1 \leq b \leq 10^5\), `g` is the return value of `func_1(a, b)` and \(g = 1\), `k` is a positive integer equal to `a + b - 1`, and \(m \geq k\)
    sum_k = k * (k + 1) // 2
    sum_m = m * (m + 1) // 2 - k * (k - 1) // 2
    return sum_k + sum_m
    #`The program returns (a + b - 1) * (a + b) // 2 + m * (m + 1) // 2 - (a + b - 1) * (a + b - 2) // 2`
#Overall this is what the function does:The function `func_2` accepts three parameters: `m` (a non-negative integer such that \(1 \leq m \leq 10^9\)), `a` (a positive integer such that \(1 \leq a \leq 10^5\)), and `b` (a positive integer such that \(1 \leq b \leq 10^5\)). It first calls another function `func_1(a, b)` to get `g`. If `g` is not 1, it recursively calls `func_2` with `m // g`, `a // g`, and `b // g`, and multiplies the result by `g`. If `m` is less than `k` (where `k` is `a + b - 1`), it returns \((m + 1) * (m + 2) // 2\). Otherwise, it calculates and returns \((a + b - 1) * (a + b) // 2 + m * (m + 1) // 2 - (a + b - 1) * (a + b - 2) // 2\).

