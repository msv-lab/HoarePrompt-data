def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t, w, b = map(int, input().split())
g = gcd(w, b)
lcm = w * b // g
count = t // lcm
res = count * (lcm // w) * (lcm // b)
print(f"{res}/{t}")
