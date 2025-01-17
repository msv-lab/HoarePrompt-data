def func_1(n, a):
    MOD = 998244353
    total_value = 0
    for mask in range(1 << n):
        max_balls = 0
        for i in range(n):
            if mask & 1 << i != 0:
                max_balls = max(max_balls, a[i])
        total_value = (total_value + max_balls) % MOD
    return total_value
n = int(input())
a = list(map(int, input().split()))
result = func_1(n, a)
print(result)