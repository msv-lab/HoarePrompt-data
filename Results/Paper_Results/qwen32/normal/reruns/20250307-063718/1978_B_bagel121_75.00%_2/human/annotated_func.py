#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers n, a, and b such that 1 <= n, a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: 
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It then calculates and prints a value based on these inputs, which is the sum of the minimum cost to select `n` items where the first `k` items (up to `b - a + 1` or `n`) are selected at costs from `b` down to `b-k+1`, and the remaining items (if any) are selected at cost `a`.

