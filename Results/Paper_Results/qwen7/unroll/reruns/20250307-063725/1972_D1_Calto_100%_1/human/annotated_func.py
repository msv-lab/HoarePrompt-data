#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: a and b will be the greatest common divisor (GCD) of the initial values of a and b.
    #
    #Explanation: The given loop implements the Euclidean algorithm for finding the greatest common divisor (GCD) of two numbers. Initially, `a` and `b` are positive integers within specified ranges. After the loop completes, `a` and `b` will hold the GCD of their initial values.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b.
#Overall this is what the function does:The function accepts two positive integers `a` and `b` as input. It computes their greatest common divisor (GCD) using the Euclidean algorithm and returns this value. Regardless of the initial values of `a` and `b`, the function ensures that upon completion, the returned value is the GCD of the original `a` and `b`.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: cnt is -1.
    return cnt
    #The program returns -1
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (with constraints 1 ≤ n, m ≤ 2⋅10^6) and iterates through a loop from 1 to `m`. For each iteration, it calculates values `x` and `y` based on the current loop index `i`. It then updates a counter `cnt` by adding the ceiling of `x` divided by `y` plus an additional 1 if `x` is exactly divisible by `y`. After completing the loop, the function returns -1.

