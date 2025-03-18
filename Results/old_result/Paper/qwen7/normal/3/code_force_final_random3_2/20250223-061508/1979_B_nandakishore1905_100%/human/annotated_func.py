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
        
    #State: After all iterations of the loop have finished, the value of `i` will be equal to the number of test cases provided as input. For each test case, the variables `n` and `m` will hold the last pair of integers entered for that test case. The variable `k` will be the absolute difference between `n` and `m` for the last test case. If `k` is a power of 2, it remains unchanged. If `k` is odd, it remains 1. If `k` is even and not a power of 2, after processing through the while loop, `k` will become 0, and `l` will be "0", `p` will be 1, and `q` will be 2.
#Overall this is what the function does:The function processes a series of test cases, each containing two distinct non-negative integers `n` and `m`. It calculates the absolute difference `k` between `n` and `m` for each test case. Depending on the value of `k`, it prints one of three possible values: `k` itself if it is a power of 2, 1 if `k` is odd, or 0 if `k` is even and not a power of 2. After processing all test cases, the function does not return any value but prints the result for each test case.

