mod = 998244353

def calculate_ways(N, d):
    if N < 2:
        return 0
    
    total_ways = 0
    
    # Calculate the sum of all d_i
    for i in range(N):
        total_ways = (total_ways + d[i]) % mod
    
    # Each connecting component can be used in 2 ways, so multiply by 2^(N-1)
    total_ways = (total_ways * pow(2, N-1, mod)) % mod
    
    return total_ways

N = int(input())
d = list(map(int, input().split()))

result = calculate_ways(N, d)
print(result)