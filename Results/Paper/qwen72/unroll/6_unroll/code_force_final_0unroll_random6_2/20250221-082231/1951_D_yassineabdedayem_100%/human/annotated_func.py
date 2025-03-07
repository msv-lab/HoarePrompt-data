#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18.
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
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n` and `k` have been read from the input. The loop has printed 'YES' followed by 1 and 1 if `n` equals `k`, printed 'YES' followed by 2 and the values `n - k + 1` and 1 if `n + 2` is greater than `k * 2`, and printed 'NO' otherwise. The values of `t`, `n`, and `k` are unchanged after the loop, but the input stream has been consumed for `t` lines.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18) from the input. It then checks if `n` equals `k`. If true, it prints 'YES' followed by 1 and 1. If `n + 2` is greater than `k * 2`, it prints 'YES' followed by 2 and the values `n - k + 1` and 1. Otherwise, it prints 'NO'. After processing all `t` test cases, the function completes, and the input stream has been consumed for `t` lines. The values of `t`, `n`, and `k` remain unchanged, but the input stream is advanced.

