a, b = map(int, input().split())
c, d = map(int, input().split())

det = a * d - b * c

if det == 0:
    print(0)
else:
    norm = max(abs(a), abs(b), abs(c), abs(d))
    print(min(1, norm / abs(det)))
