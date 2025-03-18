#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, which is stored in variable a. Since b is 0, the GCD is the initial value of a.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It calculates and returns the greatest common divisor (GCD) of these two numbers.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: cnt is the final value after the loop completes all iterations, starting from an initial value of -1.
    return cnt
    #The program returns the final value of `cnt` after the loop completes all iterations, starting from an initial value of -1.
#Overall this is what the function does:The function `func_2` takes two positive integer parameters `n` and `m` and returns a computed integer value `cnt` after performing a series of calculations involving a loop. The final value of `cnt` is determined by iterating from 1 to `m`, updating `cnt` based on the values of `n` and the loop variable `i`.

