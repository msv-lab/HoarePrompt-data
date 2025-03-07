#State of the program right berfore the function call: Each test case consists of two distinct non-negative integers x and y such that 0 <= x, y <= 10^9 and x != y. There are t test cases where 1 <= t <= 10^4.
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
        
    #State: A sequence of outputs for each pair of integers (n, m) processed by the loop, where each output is determined by the conditions on k as described.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two distinct non-negative integers `n` and `m`. For each pair, it calculates the absolute difference `k` and then determines and prints a specific value based on the properties of `k`. The printed value is either `k` if `k` is a power of two, `1` if `k` is odd, or the largest power of two less than or equal to the remainder when `k` is reduced by the largest power of two less than `k`, iteratively until the remainder itself is a power of two.

