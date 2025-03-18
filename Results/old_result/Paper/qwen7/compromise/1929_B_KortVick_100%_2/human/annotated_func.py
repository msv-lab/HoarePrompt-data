#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: The output state will consist of `t` lines, where each line contains either `k // 2 + 1` or `ceil(k / 2)`. Specifically, for each iteration of the loop, if `4 * n - 2 == k`, the output will be `k // 2 + 1`; otherwise, the output will be `ceil(k / 2)`. The value of `t` is determined by the initial input, and each subsequent input pair `(n, k)` dictates the specific output for that iteration.
#Overall this is what the function does:The function processes a series of test cases defined by the number of tests \( t \). For each test case, it reads two integers \( n \) and \( k \), and outputs either \( \lceil k / 2 \rceil \) or \( k // 2 + 1 \) based on whether \( 4n - 2 \) equals \( k \). The final state of the program consists of \( t \) lines of output, each corresponding to one test case.

