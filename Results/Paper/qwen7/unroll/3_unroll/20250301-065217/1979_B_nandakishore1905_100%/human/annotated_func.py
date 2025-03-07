#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: Output State: The output state will consist of a series of integers printed for each test case. For each test case, the value of `k` (which is `abs(n - m)`) will be processed through the conditions in the loop. If `k` is a power of 2, it will print `k`. If `k` is odd, it will print `1`. If `k` is even and not a power of 2, it will find the largest power of 2 less than or equal to `k`, subtract it from `k`, and continue this process until `k` becomes a power of 2 or 1, then print the final value of `k`.
    #
    #In mathematical terms, the output will be either the largest power of 2 less than or equal to `k` or `1` if no such power exists.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \(n\) and \(m\). For each test case, it calculates the absolute difference \(k = |n - m|\). Depending on the value of \(k\), it prints one of three possible values: \(k\) itself if it is a power of 2, 1 if \(k\) is odd, or the largest power of 2 less than or equal to \(k\) if \(k\) is even but not a power of 2. The function does not return any value but outputs these results for each test case.

