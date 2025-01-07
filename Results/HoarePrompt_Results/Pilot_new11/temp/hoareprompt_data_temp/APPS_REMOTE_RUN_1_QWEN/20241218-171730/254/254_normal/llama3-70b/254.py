k1, k2, k3 = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

lcm = k1 * k2 * k3 // (gcd(k1, k2) * gcd(k2, k3) * gcd(k1, k3))

if lcm % k1 == 0 and lcm % k2 == 0 and lcm % k3 == 0:
    print("YES")
else:
    print("NO")
