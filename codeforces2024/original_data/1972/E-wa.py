def lowbit(x):
    return x & (-x)

MOD = 998244353
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    
    # Reverse engineering f
    for _ in range(k):
        a = [0] * n
        for j in range(n):
            a[j] = (b[j] - (a[j - lowbit(j)] if j >= lowbit(j) else 0)) % MOD
        
        # Updating b for next iteration
        b = a[:]
    
    print(*a)