#State of the program right berfore the function call: Each test case consists of two distinct non-negative integers x and y such that 0 ≤ x, y ≤ 10^9 and x ≠ y. There are t test cases where 1 ≤ t ≤ 10^4.
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
        
    #State: A series of integers printed for each test case, where each integer is determined by the logic described above for the corresponding pair of integers (n, m).
#Overall this is what the function does:The function processes `t` test cases, each consisting of two distinct non-negative integers `n` and `m`. For each test case, it calculates the absolute difference `k` between `n` and `m` and then determines the smallest power of 2 that is greater than or equal to `k` if `k` is not already a power of 2. If `k` is odd, it outputs `1`. Otherwise, it outputs the largest power of 2 less than or equal to `k`.

