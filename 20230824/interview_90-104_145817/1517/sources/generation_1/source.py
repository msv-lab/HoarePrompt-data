n = int(input())
mod = 1000000007
result = ((n+1)**n - (n**n)) % mod
print(result)