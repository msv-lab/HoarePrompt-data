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
        
    #State: Output State: The loop will continue to execute until all `i` values from `0` to `t-1` are processed. After all iterations, for each test case, the variable `k` will be reduced to its simplest form based on the given conditions. Specifically, if `k` is a power of 2, it remains unchanged. If `k` is odd, it also remains unchanged. If `k` is even and at least 14, it will be reduced to 0 through the process described in the loop. For values of `k` that are even and less than 14, they will be reduced to 0 as well, following the same logic.
    #
    #In summary, after all iterations of the loop have finished, the value of `k` for each test case will be either the original `k` if it is a power of 2 or odd, or 0 if it is even and can be reduced to 0 through the loop's operations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two distinct non-negative integers \(n\) and \(m\). For each test case, it calculates the absolute difference \(k = |n - m|\) and then simplifies \(k\) based on specific conditions. If \(k\) is a power of 2, it remains unchanged. If \(k\) is odd, it also remains unchanged. If \(k\) is even and at least 14, it is reduced to 0 through a series of operations. For even values of \(k\) less than 14, they are similarly reduced to 0. The function outputs the simplified value of \(k\) for each test case.

