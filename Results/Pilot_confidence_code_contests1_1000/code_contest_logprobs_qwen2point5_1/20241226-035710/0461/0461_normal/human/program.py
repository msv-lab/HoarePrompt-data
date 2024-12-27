t = int(raw_input())
for i in range(0, t):
    a, b = map(int, raw_input().split())
    if(b == 0):
        print(1)
        continue
    if(a == 0):
        print(0.5)
        continue
    p = a * b + max(a-4*b, 0) * b
    q = a * 2 * b
    a = min(a, 4 * b)
    p = p + a * a / 8.0
    print(p / (1.0 * q))