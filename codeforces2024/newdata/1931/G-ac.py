mod = 998244353

# Precompute factorials up to 2,000,000
f = [1]
for i in range(1, 2 * 10 ** 6 + 1):
    f.append(f[-1] * i % mod)

# Process each test case
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    
    # If the difference between a and b is more than 1, it's impossible to form a chain
    if abs(a - b) > 1:
        print(0)
    elif a == b:
        # If a and b are both zero, check if c or d is zero
        if a == 0:
            print(int((c == 0) or (d == 0)))
        else:
            # Calculate the number of ways using factorials
            result = (f[a - 1 + c] * f[a + d] + f[a - 1 + d] * f[a + c]) * pow(f[a - 1] * f[d] * f[a] * f[c], -1, mod) % mod
            print(result)
    else:
        # If a and b differ by exactly 1, calculate the number of ways
        a = max(a, b)
        result = f[a - 1 + c] * f[a - 1 + d] * pow(f[a - 1] ** 2 * f[c] * f[d], -1, mod) % mod
        print(result)