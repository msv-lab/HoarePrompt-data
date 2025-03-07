#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 1000, `_` is a placeholder variable that has been incremented by `t` times, `n` and `k` are the first and second integers in the last input line, respectively. If `n` is equal to `k`, the current values of `n` and `k` remain equal. If `n` is not equal to `k`, the condition `n + 2 > k * 2` or `n + 2 <= k * 2` holds, depending on the values of `n` and `k`.
#Overall this is what the function does:The function reads an integer `t` from the user, where `1 ≤ t ≤ 1000`. It then processes `t` pairs of integers `(n, k)` from the standard input, where each `n` and `k` are positive integers such that `1 ≤ n, k ≤ 10^18`. For each pair, the function prints 'YES' and two integers if `n` is equal to `k` or if `n + 2 > k * 2`. If neither condition is met, it prints 'NO'. After processing all `t` pairs, the function concludes. The final state of the program includes the printed results for each pair, and the input variables `t`, `n`, and `k` are no longer in use.

