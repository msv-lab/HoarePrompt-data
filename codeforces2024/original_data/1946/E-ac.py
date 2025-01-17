U = 1000000007

def pw(x, y):
    # Function to compute (x^y) % U using binary exponentiation
    v = 1
    while y:
        if y & 1:
            v = v * x % U
        y >>= 1
        x = x * x % U
    return v

# Precompute factorials and their modular inverses
fac = [1]
for i in range(1, 200001):
    fac.append(fac[-1] * i % U)

inv = [0] * 200001
inv[200000] = pw(fac[200000], U - 2)
for i in range(199999, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % U

t = int(input())
for _ in range(t):
    n, m1, m2 = [int(z) for z in input().split()]
    a1 = [int(z) for z in input().split()]
    a2 = [int(z) for z in input().split()]

    # Check initial conditions for valid permutations
    if a1[0] != 1 or a1[-1] != a2[0] or a2[-1] != n:
        print(0)
    else:
        m = a2[0]
        l = m - 1
        r = n - m
        # Calculate initial number of permutations
        v = fac[n - 1] * inv[l] * inv[r] % U

        # Process prefix maximums
        for i in range(m1 - 2, -1, -1):
            dx = a1[i + 1] - a1[i] - 1
            # Update number of permutations for this segment
            v = v * fac[l - 1] * inv[l - 1 - dx] % U
            l = a1[i] - 1

        # Process suffix maximums
        for i in range(m2 - 1):
            dx = a2[i + 1] - a2[i] - 1
            # Update number of permutations for this segment
            v = v * fac[r - 1] * inv[r - 1 - dx] % U
            r = n - a2[i + 1]

        # Output the result for the current test case
        print(v)