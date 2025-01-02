le = sys.__stdin__.read().split('\n')[::-1]
mo = 10 ** 9 + 7
if 1:
    n = int(le.pop())
    c = list(map(int, le.pop().split()))
    b = list(map(int, le.pop().split()))
    le.pop()
    x = int(le.pop())
    prefb = [b[0]]
    for k in b[1:]:
        prefb.append(k + prefb[-1])
    prefb.append(0)
    prefbt = [0]
    for k in range(1, n - 1):
        prefbt.append(k * b[k] + prefbt[-1])
    prefbt.append(0)
sc = sum(c)
d = [[0] * (sc + 1) for k in range(n + 1)]
ds = [[0] * (sc + 2) for k in range(n + 1)]
ds[-1] = list(range(sc + 2))
d[-1] = [1] * (sc + 1)
for index in range(n - 1, -1, -1):
    minpref = 0
    while (minpref - index * prefb[index - 1] + prefbt[index - 1]) / (index + 1) < x:
        minpref += 1
    for pref in range(sc + 1):
        mi = min(pref + c[index] + 1, sc + 1)
        ma = max(minpref, pref)
        d[index][pref] = 0 if mi < ma else ds[index + 1][mi] - ds[index + 1][ma]
    for pref in range(1, sc + 2):
        ds[index][pref] = (ds[index][pref - 1] + d[index][pref - 1]) % mo
print(d[0][0] % mo)