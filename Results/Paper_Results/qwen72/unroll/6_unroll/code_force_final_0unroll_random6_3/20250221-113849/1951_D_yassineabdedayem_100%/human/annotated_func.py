#State of the program right berfore the function call: t is an integer such that 1 \le t \le 1000, and for each test case, n and k are positive integers such that 1 \le n, k \le 10^{18}.
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
        
    #State: The loop has completed all its iterations, and the values of `t`, `n`, and `k` are unchanged. The loop has printed 'YES' followed by 1 and 1 if `n` equals `k`, or 'YES' followed by 2 and the values of `n - k + 1` and 1 if `n + 2 > k * 2`, or 'NO' if neither condition is met, for each of the `t` test cases.
#Overall this is what the function does:The function `func` reads an integer `t` (where \(1 \le t \le 1000\)) representing the number of test cases. For each test case, it reads two positive integers `n` and `k` (where \(1 \le n, k \le 10^{18}\)). The function then prints 'YES' followed by 1 and 1 if `n` equals `k`, or 'YES' followed by 2 and the values of `n - k + 1` and 1 if `n + 2 > k * 2`, or 'NO' if neither condition is met. After processing all test cases, the values of `t`, `n`, and `k` are unchanged.

