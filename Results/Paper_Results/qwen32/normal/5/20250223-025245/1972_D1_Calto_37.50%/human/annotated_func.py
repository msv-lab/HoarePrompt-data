#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the greatest common divisor of the original values of `a` and `b`; `b` is 0.
    return a
    #The program returns the greatest common divisor of the original values of `a` and `b`
#Overall this is what the function does:The function accepts two positive integer parameters and returns their greatest common divisor.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: cnt is `n + (m - 2) + sum((n - (k^2 - k)) // (k^2) for k in range(2, m))`
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is `n + (m - 2) + sum((n - (k^2 - k)) // (k^2) for k in range(2, m))`, and `cnt` is not equal to 0
    return cnt
    #The program returns `cnt`, which is calculated as `n + (m - 2) + sum((n - (k^2 - k)) // (k^2) for k in range(2, m))` and is not equal to 0
#Overall this is what the function does:The function `func_2` takes two positive integer parameters `n` and `m` and calculates a value `cnt` using a specific formula. If `cnt` equals 0, the function returns 1. Otherwise, it returns the calculated value of `cnt`.

