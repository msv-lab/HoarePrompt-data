import sys
import random

def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(map(int, input().strip()))
        a.append(row)

    def rng():
        return random.randint(0, sys.maxsize)

    INF = 4 * 10**18
    h = [rng() % INF for _ in range(n)]

    ans = 0
    dp = {}
    used = set()
    for j in range(m):
        hash_val = 0
        for i in range(n):
            if a[i][j]:
                hash_val ^= h[i]
        for i in range(n):
            hash_val ^= h[i]
            dp[hash_val] = dp.get(hash_val, 0) + 1
            if dp[hash_val] > ans:
                ans = dp[hash_val]
                used.clear()
                for k in range(n):
                    if k == i:
                        if a[k][j] == 0:
                            used.add(k)
                    else:
                        if a[k][j]:
                            used.add(k)
            hash_val ^= h[i]

    print(ans)
    print(''.join('1' if i in used else '0' for i in range(n)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
