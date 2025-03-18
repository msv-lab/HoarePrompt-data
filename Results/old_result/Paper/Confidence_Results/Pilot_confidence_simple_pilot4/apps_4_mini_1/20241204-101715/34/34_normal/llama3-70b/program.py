def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a1, b1, a2, b2, L, R = map(int, input().split())
gcd_val = gcd(a1, a2)
lcm_val = a1 * a2 // gcd_val
start = max((L - b1) // a1, (L - b2) // a2)
end = min((R - b1) // a1, (R - b2) // a2)
count = 0
for k in range(start, end + 1):
    if (a1 * k + b1 - b2) % a2 == 0 and L <= a1 * k + b1 <= R:
        count += 1
print(count)
