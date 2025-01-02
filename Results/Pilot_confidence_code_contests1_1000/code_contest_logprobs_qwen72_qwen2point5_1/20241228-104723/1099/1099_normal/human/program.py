N, M = map(int, raw_input().split())
S = [i for i in raw_input()]
T = [i for i in raw_input()]

data = []
for i in range(1, N*M):
    ma = max([N, M])
    mi = min([N, M])

    if i * ma % mi == 0:
        data.append(i * ma)
    if i * ma > N*M:
        break

for d in data:
    slist = [j * d / N + 1  for j in range(d)][:N]
    tlist = [j * d / M + 1  for j in range(d)][:M]

    result = []
    for j in [j for j in slist if j in tlist]:
        result.append(S[slist.index(j)] == T[tlist.index(j)])
    if all(result):
        print(d)
        exit(0)

print(-1)
