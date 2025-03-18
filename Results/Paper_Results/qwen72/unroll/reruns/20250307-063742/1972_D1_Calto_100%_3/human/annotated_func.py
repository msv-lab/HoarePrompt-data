#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `cnt` is the number of integers `i` in the range [1, m] such that `n - (i * i - i)` is divisible by `i * i`, minus 1.
    return cnt
    #The program returns the number of integers `i` in the range [1, m] such that `n - (i * i - i)` is divisible by `i * i`, minus 1.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` and returns the count of integers `i` in the range [1, m] such that `n - (i * i - i)` is divisible by `i * i`, minus 1. After the function concludes, `cnt` holds this computed value.

