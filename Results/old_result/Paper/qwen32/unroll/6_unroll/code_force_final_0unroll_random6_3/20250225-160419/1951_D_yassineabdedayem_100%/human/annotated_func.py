#State of the program right berfore the function call: Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^{18}) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.
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
        
    #State: `t` remains the same as the initial input integer, while `n` and `k` are the values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` and `k`. For each test case, it determines if it's possible to buy exactly `k` jewels with `n` coins, and outputs "YES" along with the number of coins spent and the number of coins left if possible, otherwise it outputs "NO".

