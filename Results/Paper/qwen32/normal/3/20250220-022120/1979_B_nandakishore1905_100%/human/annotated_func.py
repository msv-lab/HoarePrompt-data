#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif k % 2 != 0:
            print(1)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = k - q
            while f & f - 1 != 0:
                l = bin(f).replace('0b', '')
                p = len(l)
                q = 2 ** (p - 1)
                f = f - q
            print(f)
        
    #State: A series of printed values, one for each test case, based on whether the absolute difference `k` is a power of 2, odd, or even and not a power of 2.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it accepts two distinct non-negative integers `x` and `y`. It then calculates the absolute difference between `x` and `y` and prints a value based on whether this difference is a power of 2, odd, or even and not a power of 2. Specifically, if the difference is a power of 2, it prints the difference. If the difference is odd, it prints 1. If the difference is even and not a power of 2, it prints the largest power of 2 less than the difference.

