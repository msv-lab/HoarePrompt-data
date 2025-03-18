#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, the variable `a` holds the GCD of the initial values of `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` remain unchanged, `cnt` is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + (n - (i * i - i)) % (i * i) == 0` for `i` from 1 to `m`.
    return cnt
    #The program returns the sum of `math.ceil((n - (i * i - i)) / (i * i)) + (n - (i * i - i)) % (i * i) == 0` for `i` from 1 to `m`. This sum is calculated based on the initial values of `n` and `m`, and it represents the total count of a specific condition being met for each `i` in the range from 1 to `m`.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` and returns an integer `cnt`. The value of `cnt` is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + (n - (i * i - i)) % (i * i) == 0` for each integer `i` from 1 to `m`. The function does not modify the input parameters `n` and `m`. After the function concludes, `cnt` represents the total count of a specific condition being met for each `i` in the range from 1 to `m`.

