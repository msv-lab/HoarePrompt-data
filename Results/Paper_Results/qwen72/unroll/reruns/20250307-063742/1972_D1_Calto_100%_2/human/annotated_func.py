#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, both of which are positive integers. It returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD of the initial values of `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: - `n` remains the same.
    #   - `m` remains the same.
    #   - `cnt` will be the result of the loop's computation.
    #
    #Given the initial state and the loop's behavior, the output state can be described as:
    #
    #Output State:
    return cnt
    #The program returns the value of `cnt` which is the result of the loop's computation.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) and returns an integer `cnt`. The value of `cnt` is computed by iterating through the range from 1 to `m` inclusive, where for each iteration, it calculates a value based on `n` and the current iteration index `i`, and updates `cnt` accordingly. After the loop completes, `n` and `m` remain unchanged, and the function returns the final value of `cnt`.

