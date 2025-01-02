input = sys.stdin.readline
n = int(input())
seq = sorted(((int(x) - i, int(x)) for (i, x) in enumerate(input().split())), key=lambda x: x[0])
d = dict()
ans = 0
ansb = 0
for (g, val) in seq:
    try:
        d[abs(g)] += val
    except:
        d[abs(g)] = val
    ans = max(ans, d[abs(g)])
    ansb = max(val, ansb)
if ans == 0:
    ans = ansb
print(ans)