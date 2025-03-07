#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the GCD of the initial `a` and `b`; `b` is 0.
    return a
    #The program returns the GCD of the initial `a` and `b`, which is `a` since `b` is 0.
#Overall this is what the function does:The function calculates and returns the greatest common divisor (GCD) of the two input positive integers `a` and `b`.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `cnt` is updated to `-1 + sum(math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0) for i in range(1, m + 1))
    return cnt
    #The program returns `cnt` which is updated to `-1 + sum(math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0) for i in range(1, m + 1))`
#Overall this is what the function does:The function accepts two positive integer parameters `n` and `m`, and returns a count `cnt` which is calculated based on a summation involving the ceiling of a division and a condition check for each integer `i` from 1 to `m`. Specifically, for each `i`, it computes a value and accumulates it into `cnt`, which is then adjusted by subtracting 1 from the total sum.

