n, m = map(int, input().split())
mem = {}
for _ in range(m):
    k, f = map(int, input().split())
    mem[k] = f

gcd = None
for k, f in mem.items():
    if gcd is None:
        gcd = k
    else:
        gcd = math.gcd(gcd, k)

if gcd == 1:
    print(-1)
else:
    for k, f in mem.items():
        n_floor = (n - 1) // (k // gcd) + 1
        if n_floor == f:
            print(n_floor)
            break
    else:
        print(-1)
