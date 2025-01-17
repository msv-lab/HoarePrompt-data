def count_ways(n, m):
    MOD = 10**9 + 7
    ways = [0]*(m+1)
    ways[0] = 1
    for _ in range(n):
        new_ways = [0]*(m+1)
        for i in range(m+1):
            new_ways[i] += ways[i]
            if i > 0:
                new_ways[i] += ways[i-1]*i
            new_ways[i] %= MOD
        ways = new_ways
    return ways[m]

n, m = map(int, input().split())
print(count_ways(n, m))
