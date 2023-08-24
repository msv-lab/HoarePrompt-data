mod = 998244353

def calculate_ways(N, d):
    total_ways = 1
    
    # Calculate the product of all d_i
    for i in range(N):
        total_ways = (total_ways * d[i]) % mod
    
    # Each connecting component can be used in 2 ways, so multiply by 2^(N-2)
    total_ways = (total_ways * pow(2, N-2, mod)) % mod
    
    return total_ways

N = int(input())
d = list(map(int, input().split()))

result = calculate_ways(N, d)
print(result)