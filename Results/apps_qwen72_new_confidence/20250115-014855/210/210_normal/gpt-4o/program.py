MOD = 1000000007

# Read inputs
x, y = map(int, input().split())
n = int(input())

# Calculating the term based on the periodicity of 6
terms = [x, y, y - x, -x, -y, x - y]
result = terms[(n - 1) % 6] % MOD

# Adjusting for negative results to ensure positive modulo results
if result < 0:
    result += MOD

print(result)
