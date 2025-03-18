#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The output state is that `a` contains the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` is 0.
    #
    #The loop implements the Euclidean algorithm, which finds the GCD of two numbers. In each iteration, `a` is updated to `b`, and `b` is updated to the remainder of `a` divided by `b`. This process continues until `b` becomes 0, at which point `a` holds the GCD of the original values of `a` and `b`.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It computes their greatest common divisor (GCD) using the Euclidean algorithm and returns this value. After execution, `a` contains the GCD of the initial values of `a` and `b`, while `b` is guaranteed to be 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: cnt is -1.
    return cnt
    #The program returns -1
#Overall this is what the function does:The function accepts two positive integers, n and m, as input. It initializes a counter `cnt` to -1. For each integer `i` from 1 to `m`, it calculates values `x` and `y` based on `n` and `i`. It then updates the counter `cnt` by adding the result of `math.ceil(x / y)` plus an additional 1 if `x` is exactly divisible by `y`. Finally, the function returns the counter `cnt`, which is always -1 regardless of the input values.

