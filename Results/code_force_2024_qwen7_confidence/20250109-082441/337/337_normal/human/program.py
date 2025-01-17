def solve(n, a):
    MOD = 998244353
    total_value = 0
    
    # Iterate over all subsets of colors
    for mask in range(1 << n):
        max_balls = 0
        for i in range(n):
            if (mask & (1 << i)) != 0:
                max_balls = max(max_balls, a[i])
        total_value = (total_value + max_balls) % MOD
    
    return total_value

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Solve the problem
result = solve(n, a)
print(result)