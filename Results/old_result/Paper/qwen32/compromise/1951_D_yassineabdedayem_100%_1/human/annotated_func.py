#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are positive integers such that 1 <= n, k <= 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: The output state consists of a series of 'YES' or 'NO' responses, each followed by additional output lines based on the conditions evaluated within the loop. For each test case, if n equals k, the output is 'YES', 1, and 1. If n + 2 is greater than k * 2, the output is 'YES', 2, n - k + 1, and 1. Otherwise, the output is 'NO'. The values of n, k, and t remain unchanged in the initial state, and t iterations of the loop have been executed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two positive integers `n` and `k`. For each test case, it determines if it's possible to satisfy certain conditions and prints 'YES' followed by specific values if the conditions are met, or 'NO' if they are not. The values of `n` and `k` remain unchanged after processing each test case.

