#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: The loop has processed all `t` test cases, and the variables `n`, `m`, and `k` reflect the values from the last test case. Any intermediate variables (`l`, `p`, `q`, `f`) reflect their values from the last iteration where they were used.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two distinct non-negative integers. For each test case, it calculates a value based on the absolute difference between the two integers and prints a specific result. The result is the largest power of 2 that divides the absolute difference if it is a power of 2, 1 if the difference is odd, or a derived value if the difference is even and not a power of 2.

