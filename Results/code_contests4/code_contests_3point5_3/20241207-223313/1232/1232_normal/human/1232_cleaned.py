stdin = BytesIO(os.read(0, os.fstat(0).st_size))
stdout = BytesIO()
res = []
inp = stdin.readlines()
T = int(inp[0])
_i = 1
for t in range(T):
    N = int(inp[_i])
    _i += 1
    monsters = []
    mnShots = 0
    start = maxint
    for n in range(N):
        cur = map(int, inp[_i].split())
        _i += 1
        monsters.append(cur)
        if n > 0:
            dam = max(0, cur[0] - monsters[n - 1][1])
            mnShots += dam
            start = min(start, cur[0] - dam)
    dam = max(0, monsters[0][0] - monsters[-1][1])
    mnShots += dam
    start = min(start, monsters[0][0] - dam)
    res.append(mnShots + start)
os.write(1, '\n'.join((str(x) for x in res)))