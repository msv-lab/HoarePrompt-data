#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x ≠ y.
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
        
    #State: The values of x and y remain unchanged. The loop processes each pair of integers (n, m) provided as input and prints a specific value based on the conditions described in the loop. The loop does not modify x and y.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It processes a series of pairs of integers (n, m) provided through standard input. For each pair, it calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `k` is odd, it prints 1. If `k` is even and not a power of 2, it performs additional calculations to find the largest power of 2 less than `k` and prints the result of subtracting this power of 2 from `k`. The function does not modify any external variables.

