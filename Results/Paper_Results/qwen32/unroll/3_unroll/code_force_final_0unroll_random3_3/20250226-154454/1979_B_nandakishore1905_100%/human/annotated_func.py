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
        
    #State: For each test case, the output will be an integer based on the conditions: the absolute difference `k` if it's a power of 2, `1` if `k` is odd, or the largest power of 2 less than or equal to `k` if `k` is neither a power of 2 nor odd.
#Overall this is what the function does:The function processes a number of test cases, each consisting of two distinct non-negative integers. For each test case, it calculates the absolute difference between the two integers and then determines the output based on specific conditions: if the difference is a power of 2, it outputs the difference; if the difference is odd, it outputs 1; otherwise, it outputs the largest power of 2 that is less than or equal to the difference.

