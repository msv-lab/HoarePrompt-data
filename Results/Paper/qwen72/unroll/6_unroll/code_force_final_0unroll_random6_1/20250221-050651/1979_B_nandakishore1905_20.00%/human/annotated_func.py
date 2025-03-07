#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9. The loop has no effect on the values of x and y.
#Overall this is what the function does:The function `func` reads an integer from the input, which determines the number of iterations. For each iteration, it reads two integers `n` and `m` from the input. It then calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `n` is 0 and `m` is odd, it prints 1. If `n` is 0 and `m` is even, it prints 2. Otherwise, it prints the difference between `k` and the largest power of 2 less than or equal to `k`. The function does not modify the values of `x` and `y` (which are distinct non-negative integers such that 0 <= x, y <= 10^9) and does not return any value.

