#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: The loop terminates with `a` equal to the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` equal to 0. The values of `n` and `m` remain unchanged, and `a` is still a positive integer such that 1 <= a <= n.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, which is a positive integer such that 1 <= a <= n.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` (with 1 <= a <= n and 1 <= b <= m) and returns their greatest common divisor (GCD). After the function concludes, the value of `a` is the GCD of the initial values of `a` and `b`, and `b` is 0. The values of `n` and `m` remain unchanged.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `i` is `m-1`, `cnt` is the sum of `n + (n - (i * i - i)) // (i * i) + (i > 1)` for each `i` from 1 to `m-1`.
    if (cnt == 0) :
        return 1
        #The program returns 1.
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `i` is `m-1`, `cnt` is the sum of `n + (n - (i * i - i)) // (i * i) + (i > 1)` for each `i` from 1 to `m-1`, and `cnt` is not equal to 0.
    return cnt
    #The program returns the sum of `n + (n - (i * i - i)) // (i * i) + (i > 1)` for each `i` from 1 to `m-1`. Here, `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, and `i` is `m-1`. The value of `cnt` is not equal to 0.
#Overall this is what the function does:The function `func_2` accepts two positive integers, `n` and `m`, where 1 <= n, m <= 2 * 10^6. It returns 1 if the sum of a series of calculations based on `n` and `m-1` is zero. Otherwise, it returns the sum of these calculations, which is the sum of `n + (n - (i * i - i)) // (i * i) + (i > 1)` for each `i` from 1 to `m-1`. The final state of the program includes the unchanged values of `n` and `m`, and the computed value of `cnt` which is returned.

