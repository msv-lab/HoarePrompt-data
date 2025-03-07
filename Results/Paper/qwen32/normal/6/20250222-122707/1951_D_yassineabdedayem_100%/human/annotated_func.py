#State of the program right berfore the function call: Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^{18}) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. The input consists of multiple test cases, with the first line containing an integer t (1 ≤ t ≤ 1000) indicating the number of test cases.
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
        
    #State: The loop has executed `t` times, and for each test case, it has printed either "YES" followed by two integers or "NO" based on the relationship between `n` and `k`. The values of `t`, `n`, and `k` from the input remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` and `k`. It determines whether Alice can buy exactly `k` jewels with her `n` coins and prints "YES" followed by two integers if possible, or "NO" if not.

