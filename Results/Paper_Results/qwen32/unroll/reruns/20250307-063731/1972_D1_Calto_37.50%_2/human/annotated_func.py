#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the GCD of the initial values of a and b, and b is 0.
    return a
    #The program returns a, which is the greatest common divisor of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function calculates and returns the greatest common divisor (GCD) of the two input positive integers `a` and `b`.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: cnt is the sum of n and the series \(\sum_{i=2}^{m-1} \left( \frac{n}{i^2} + \frac{1}{i} \right)\).
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: cnt is the sum of n and the series \(\sum_{i=2}^{m-1} \left( \frac{n}{i^2} + \frac{1}{i} \right)\), and cnt is not equal to 0.
    return cnt
    #The program returns `cnt` which is the sum of `n` and the series \(\sum_{i=2}^{m-1} \left( \frac{n}{i^2} + \frac{1}{i} \right)\)
#Overall this is what the function does:The function accepts two positive integer parameters `n` and `m` where 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6. It calculates a value `cnt` as the sum of a series involving `n` and `m`. If `cnt` is 0, it returns 1. Otherwise, it returns `cnt`.

