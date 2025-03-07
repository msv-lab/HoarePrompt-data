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
        
    #State: a series of printed values, one for each test case, based on the logic described above.
#Overall this is what the function does:The function `func` processes `t` test cases, where each test case consists of two distinct non-negative integers `n` and `m`. For each test case, it calculates the absolute difference `k` between `n` and `m` and prints a specific value based on the properties of `k`. The printed value is either `k` if `k` is a power of 2, `1` if `k` is odd, or the largest power of 2 less than or equal to `k` if `k` is even and not a power of 2.

