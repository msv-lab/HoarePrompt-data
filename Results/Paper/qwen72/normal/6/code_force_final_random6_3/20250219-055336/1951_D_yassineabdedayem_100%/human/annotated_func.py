#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
        
    #State: `t` is 0, `_` is `t - 1`, `n` and `k` are the last set of input integers. If `n` is equal to `k`, the condition `n == k` holds. If `n` is not equal to `k`, and `n + 2` is greater than `k * 2`, the condition `n + 2 > k * 2` holds. Otherwise, `n + 2` is less than or equal to `k * 2`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases (1 ≤ t ≤ 1000). For each test case, it reads two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). The function then checks if `n` is equal to `k`. If so, it prints 'YES' followed by two lines containing the number 1. If `n` is not equal to `k` but `n + 2` is greater than `k * 2`, it prints 'YES' followed by two lines: the first line contains `n - k + 1` and the second line contains 1. If neither condition is met, it prints 'NO'. After processing all test cases, the function concludes with `t` being 0, `_` being `t - 1`, and `n` and `k` being the last set of input integers for the final test case.

