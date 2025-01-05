sys.stdin = BytesIO(sys.stdin.read())
input = lambda : sys.stdin.readline().rstrip('\r\n')
(n, m, D) = [int(x) for x in input().split(' ')]
ds = defaultdict(set)
dmain = defaultdict(set)
for i in range(m):
    (s, f) = [int(x) for x in input().split(' ')]
    if s != 1 and f != 1:
        ds[s].add(f)
        ds[f].add(s)
    dmain[s].add(f)
    dmain[f].add(s)
if len(dmain[1]) < D:
    print('NO')
    exit()
arr = [0] * (n + 1)
i = 2
cur = 0
while i < n:
    if arr[i] == 0:
        cur += 1
        tov = {i}
        arr[i] = cur
        while len(tov):
            nxt = tov.pop()
            for el in ds[nxt]:
                if arr[el] == 0:
                    arr[el] = cur
                    tov.add(el)
    i += 1
if cur > D:
    print('NO')
    exit()
sviaz = set()
ite = dmain[1].copy()
for el in ite:
    if arr[el] not in sviaz:
        sviaz.add(arr[el])
    else:
        dmain[el].remove(1)
        dmain[1].remove(el)
sv = set()
sv.add(1)
vis = set()
vis.add(1)
res = ['YES']
while len(sv):
    nxt = sv.pop()
    for el in dmain[nxt]:
        if el not in vis:
            sv.add(el)
            vis.add(el)
            res.append(str(nxt) + ' ' + str(el))
        dmain[el].remove(nxt)
print('\n'.join(res))