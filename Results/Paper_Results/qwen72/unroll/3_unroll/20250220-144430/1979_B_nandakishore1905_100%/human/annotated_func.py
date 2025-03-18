#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x != y.
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
        
    #State: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x != y. The loop has processed the input values and printed the results, but the values of x and y remain unchanged.
#Overall this is what the function does:The function `func` processes a series of pairs of non-negative integers `(n, m)` provided by the user. For each pair, it calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `k` is odd, it prints `1`. If `k` is even but not a power of 2, it prints the largest power of 2 that is less than or equal to `k` and can be subtracted from `k` to result in a power of 2. The function does not modify any external variables or parameters.

