#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor of the initial values of a and b, and since b is 0, the program returns a.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `a` and `b`. It returns the greatest common divisor (GCD) of these two integers.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `cnt` is the sum of `n` and the integer divisions `(n - i * (i - 1)) // (i * i)` for `i` from 2 to `m-1`, plus `m-2`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is the sum of `n` and the integer divisions `(n - i * (i - 1)) // (i * i)` for `i` from 2 to `m-1`, plus `m-2`. Additionally, `cnt` is not equal to 0.
    return cnt
    #The program returns the value of `cnt`, which is the sum of `n` and the integer divisions `(n - i * (i - 1)) // (i * i)` for `i` from 2 to `m-1`, plus `m-2`.
#Overall this is what the function does:The function accepts two positive integer parameters `n` and `m`. It calculates a value `cnt` by summing `n` and the integer divisions `(n - i * (i - 1)) // (i * i)` for each `i` from 2 to `m-1`, plus `m-2`. If `cnt` is 0, it returns 1; otherwise, it returns the value of `cnt`.

