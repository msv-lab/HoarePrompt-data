#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the GCD of the original a and b; b is 0.
    return a
    #The program returns the GCD of the original a and b, which is now stored in a. Since b is 0, the GCD is the value of a.
#Overall this is what the function does:The function accepts two positive integers `a` and `b` and returns their greatest common divisor (GCD).

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `n` and `m` are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6; `i` is `m`; `cnt` is the accumulated sum of `(n - (i * i - i)) // (i * i) + (i > 1)` for `i` from `1` to `m - 1`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `n` and `m` are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6; `i` is `m`; `cnt` is the accumulated sum of `(n - (i * i - i)) // (i * i) + (i > 1)` for `i` from `1` to `m - 1`; `cnt` is not equal to 0
    return cnt
    #The program returns `cnt`, which is the accumulated sum of `(n - (i * i - i)) // (i * i) + (i > 1)` for `i` from `1` to `m - 1`.
#Overall this is what the function does:The function accepts two positive integer parameters `n` and `m` where 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6. It calculates the accumulated sum of `(n - (i * i - i)) // (i * i) + (i > 1)` for all integers `i` from 1 to `m - 1`. If this accumulated sum is zero, the function returns 1; otherwise, it returns the accumulated sum.

