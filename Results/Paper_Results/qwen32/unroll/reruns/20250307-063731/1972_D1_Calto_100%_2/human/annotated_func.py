#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the GCD of the initial values of a and b, and b is 0.
    return a
    #The program returns the GCD of the initial values of a and b, which is also the current value of a.
#Overall this is what the function does:The function accepts two positive integers `a` and `b` and returns their greatest common divisor (GCD).

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `cnt` is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from `1` to `m`, starting from the initial value of `-1`.
    return cnt
    #The program returns `cnt`, which is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from `1` to `m`, starting from the initial value of `-1`.
#Overall this is what the function does:The function accepts two positive integer parameters `n` and `m` and returns a calculated sum `cnt`. This sum is computed by iterating over each integer `i` from 1 to `m`, and for each `i`, it adds the value of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` to `cnt`. The initial value of `cnt` is `-1`.

