from sys import stdin

n, l, k = map(int, stdin.readline().split())
s, out = sorted(stdin.readline().strip())[::-1], [[] for _ in range(n)]

for i in range(l):
    for j in range(k):
        out[j].append(s.pop())

    if k == 1 or out[k - 1][-1] > out[k - 2][-1]:
        break

while len(out[k - 1]) < l:
    out[k - 1].append(s.pop())

for i in range(n):
    while len(out[i]) < l:
        out[i].append(s.pop())

print('\n'.join([''.join(x) for x in out]))
